// scripts.js

document.addEventListener('DOMContentLoaded', () => {
    const imageInput = document.getElementById('image-input');
    const resultDiv = document.getElementById('result');
    const uploadForm = document.getElementById('upload-form');

    imageInput.addEventListener('change', handleImageChange);
    uploadForm.addEventListener('submit', handleFormSubmit);

    function handleImageChange(event) {
        const file = event.target.files[0];
        if (file) {
            displaySelectedFileName(file);
        }
    }

    function handleFormSubmit(event) {
        event.preventDefault();
        const formData = new FormData();
        const image = imageInput.files[0];
        formData.append('image', image);

        displayUploadedFileName(image);
        uploadImage(formData).then(displayColors).catch(handleError);
    }

    function displaySelectedFileName(file) {
        resultDiv.innerHTML = `<h2>Selected File: ${file.name}</h2>`;
    }

    function displayUploadedFileName(file) {
        resultDiv.innerHTML = `<h2>Uploaded File: ${file.name}</h2>`;
    }

    function uploadImage(formData) {
        return fetch('/upload/', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json());
    }

    function displayColors(colors) {
        resultDiv.innerHTML += '<h2>Detected Colors:</h2>';
        colors.forEach(color => {
            const colorBox = createColorBox(color);
            resultDiv.appendChild(colorBox);
        });
    }

    function createColorBox(color) {
        const colorBox = document.createElement('div');
        colorBox.className = 'color-box';
        colorBox.style.backgroundColor = `rgb(${color.r}, ${color.g}, ${color.b})`;
        colorBox.title = `rgb(${color.r}, ${color.g}, ${color.b})`;
        return colorBox;
    }

    function handleError(error) {
        console.error('Error:', error);
        resultDiv.innerHTML = '<h2>There was an error processing your request.</h2>';
    }
});
