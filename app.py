from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load recommendation data
content_df = pd.read_csv("content_recommendations.csv")
collab_df = pd.read_csv("Collaborative_Filtering_Results.csv")

# Get the list of available content IDs for dropdown
content_ids = collab_df["contentId"].tolist()

@app.route("/", methods=["GET", "POST"])
def index():
    selected_id = None
    collab_recs = []
    content_recs = []

    if request.method == "POST":
        selected_id = int(request.form["contentId"])
        
        # Get top 5 recommendations from both datasets
        collab_recs = [rec for rec in collab_df[collab_df["contentId"] == selected_id].values[0][1:] if rec != selected_id]
        content_recs = [rec for rec in content_df[content_df["contentId"] == selected_id].values[0][1:] if rec != selected_id]


    return render_template("index.html", content_ids=content_ids, selected_id=selected_id,
                           collab_recs=collab_recs, content_recs=content_recs)

if __name__ == "__main__":
    app.run(debug=True)
