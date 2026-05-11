//Recipe form image file selection display
const imageInput = document.getElementById('photo');
const selectedFile = document.getElementById('file-name');
const uploadText = document.querySelector('.photo-upload-text');

imageInput.addEventListener('change', function() {
    if (imageInput.files.length > 0) {
        const fileName = imageInput.files[0].name;
        selectedFile.textContent = `Selected file: ${fileName}`;
        uploadText.textContent = "Change Photo";
    } else {
        selectedFile.textContent = 'No file selected';
        uploadText.textContent = "Upload Photo";    }   
});