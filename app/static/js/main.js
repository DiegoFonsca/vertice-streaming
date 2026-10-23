const searchInput = document.querySelector("#searchInput");
const movieCards = document.querySelectorAll(".movie-card");
const catalogCount = document.querySelector("#catalogCount");
const emptyMessage = document.querySelector("#emptyMessage");

searchInput.addEventListener("input", function () {
  const searchTerm = searchInput.value.trim().toLowerCase();

  let visibleMovies = 0;

  movieCards.forEach(function (card) {
    const title = card.dataset.title.toLowerCase();

    const matches = title.includes(searchTerm);

    card.hidden = !matches;

    if (matches) {
      visibleMovies++;
    }
  });

  catalogCount.textContent =
    visibleMovies === 1 ? "1 título" : `${visibleMovies} títulos`;

  emptyMessage.hidden = visibleMovies !== 0;
});

const watchButton = document.querySelector("#watchButton");

watchButton.addEventListener("click", function () {
  alert("Em breve: trailer de Além do Horizonte!");
});
