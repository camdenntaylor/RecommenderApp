function fetchRecommendations() {
  const itemId = document.getElementById("itemIdInput").value;

  fetch("/get_recommendations", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ itemId }),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("contentRecs").innerText =
        data.content.join(", ");
      document.getElementById("collabRecs").innerText = data.collab.join(", ");
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
