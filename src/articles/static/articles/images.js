const imageClickListener = function (event) {
  let cardImage = event.target.closest('.card-image');
  const title = cardImage.dataset.imageTitle;
  const url = cardImage.dataset.imageUrl;
  const copied = cardImage.parentElement.querySelector('.copied');
  const imageMarkdown = `![${title}](${url})`;
  navigator.clipboard.writeText(imageMarkdown).then(r => {
    copied.classList.add('fade-in-and-out');
    setTimeout(() => {
      copied.classList.remove('fade-in-and-out');
    }, 1500);
  });
};

document.addEventListener('htmx:afterRequest', function (event) {
  let cardImages = document.querySelectorAll('.card-image');

  cardImages.forEach((cardImage) => {
    cardImage.removeEventListener('click', imageClickListener);
    cardImage.addEventListener('click', imageClickListener);
  });
});