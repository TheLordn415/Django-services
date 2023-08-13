function uploadFile() {
    const fileInput = document.getElementById('fileInput');
    const extensionText = document.getElementById('extensionText');

    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        const fileName = file.name;
        const fileExtension = fileName.split('.').pop(); // Отримуємо розширення файлу
        extensionText.textContent = `Розширення файлу: ${fileExtension}`;
    } else {
        extensionText.textContent = 'Файл не був вибраний';
    }
}