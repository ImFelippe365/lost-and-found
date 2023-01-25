const input = document.getElementById("id_image");
const imageName = document.getElementById("image_name");

input.addEventListener("change", () => {
  let inputImage = document.querySelector("input[type=file]").files[0];

  imageName.innerText = 'Arquivo selecionado: ' + inputImage.name;
});