document.addEventListener('DOMContentLoaded', function() {
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const result = document.getElementById('result');
    const previewImage = document.getElementById('preview-image');
    const predictionText = document.getElementById('prediction-text');
    const confidenceValue = document.getElementById('confidence-value');
    const probabilityFill = document.getElementById('probability-fill');

    // Handle drag and drop
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('dragover');
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.classList.remove('dragover');
    });

    dropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropZone.classList.remove('dragover');
        const file = e.dataTransfer.files[0];
        handleFile(file);
    });

    // Handle click upload
    dropZone.addEventListener('click', () => {
        fileInput.click();
    });

    fileInput.addEventListener('change', (e) => {
        const file = e.target.files[0];
        handleFile(file);
    });

    function handleFile(file) {
        if (!file.type.startsWith('image/')) {
            alert('Please upload an image file');
            return;
        }

        // Show loading state
        result.classList.remove('hidden');
        predictionText.textContent = 'Analyzing...';

        // Create form data
        const formData = new FormData();
        formData.append('file', file);

        // Preview image
        const reader = new FileReader();
        reader.onload = (e) => {
            previewImage.src = e.target.result;
        };
        reader.readAsDataURL(file);

        // Send to server
        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            // Update UI with results
            predictionText.textContent = data.prediction;
            const confidencePercent = (data.probability * 100).toFixed(2);
            confidenceValue.textContent = confidencePercent;
            probabilityFill.style.width = `${confidencePercent}%`;

            // Add appropriate color based on prediction
            probabilityFill.style.backgroundColor =
                data.prediction === 'Real' ? '#27ae60' : '#e74c3c';
        })
        .catch(error => {
            console.error('Error:', error);
            predictionText.textContent = 'Error analyzing image';
        });
    }
});