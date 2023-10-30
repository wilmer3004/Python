document.addEventListener('DOMContentLoaded', () => {
  // Hacer una solicitud para obtener las imágenes cuando la página se carga
  fetch('http://localhost:5000/imagenes', {
    method: 'GET',
  })
  .then(response => response.json())
  .then(data => {
    // Obtener el contenedor de imágenes
    const imagenesContainer = document.getElementById('imagenesContainer');

    // Recorrer las imágenes recibidas y mostrarlas en el contenedor
    data.imagenes.forEach(imagenBase64 => {
      const imgElement = document.createElement('img');
      imgElement.src = 'data:image/png;base64,' + imagenBase64;
      imagenesContainer.appendChild(imgElement);
    });
  })
  .catch(error => {
    console.error('Error:', error);
  });
});







const nombreInput = document.getElementById('nombreInput');
const fileInput = document.getElementById('fileInput');
const uploadButton = document.getElementById('uploadButton');

uploadButton.addEventListener('click', () => {
  const nombre = nombreInput.value;
  const file = fileInput.files[0];

  if (!nombre || !file) {
    console.error('Por favor, ingresa un nombre y selecciona una imagen.');
    return;
  }

  const reader = new FileReader();
  reader.onloadend = function() {
    const imagenBase64 = reader.result.split(',')[1]; // Obtener datos base64 sin el encabezado
    const data = {
      nombre: nombre,
      imagen: imagenBase64,
    };

    fetch('http://localhost:5000/upload', {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json',
      },
    })
    .then(response => response.json())
    .then(data => {
      console.log(data.message); // Mensaje desde el servidor
    })
    .catch(error => {
      console.error('Error:', error);
    });
  };

  reader.readAsDataURL(file);
});
