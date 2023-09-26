function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const extensionText = document.getElementById('extensionText');
    div_choose = document.getElementById('div-choose');

    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        const fileName = file.name;
        const fileExtension = fileName.split('.').pop(); // get file extension
        extensionText.textContent = `File extension: ${fileExtension}`;
        toggleDisabledByExtension(fileExtension);
        div_choose.removeAttribute("hidden");     // Show

    } else {
        extensionText.textContent = "File hasn't found";
    }
}

function toggleDisabledByExtension(extension) {
    var radioButtons = document.querySelectorAll('input[type="radio"]');

    var extensions1 = ['png', 'jpg', 'webp'];
    var extensions2 = ['docx', 'pdf'];
    var extensions3 = ['mp3'];

    radioButtons.forEach(function(radio) {
        var radioExtension = radio.value;
        radio.checked = false;
        if (extensions1.includes(extension)) {
            if (extensions2.includes(radioExtension) || extensions3.includes(radioExtension)) {
                radio.setAttribute('disabled', 'disabled');
            } else {
                radio.removeAttribute('disabled');
            }
        } else if (extensions2.includes(extension)) {
            if (extensions1.includes(radioExtension) || extensions3.includes(radioExtension)) {
                radio.setAttribute('disabled', 'disabled');
            } else {
                radio.removeAttribute('disabled');
            }
        } else if (extension == "mp4") {
            if (extensions3.includes(radioExtension)){
                radio.removeAttribute('disabled');
            }
            else {
                radio.setAttribute('disabled', 'disabled');
            }
        }
        if (extension === radioExtension) {
            radio.setAttribute('disabled', 'disabled');
        }
    });
}
document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('fileInput').addEventListener("change", uploadFile, false);
});