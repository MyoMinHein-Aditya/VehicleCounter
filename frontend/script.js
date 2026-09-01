async function detectVehicles() {
    const fileInput = document.getElementById('imageInput');
    const errorDiv = document.getElementById('errorMessage');
    const resultsSection = document.getElementById('resultsSection');
    
    errorDiv.innerText = "";
    resultsSection.classList.add('results-hidden');

    if (!fileInput.files[0]) {
        errorDiv.innerText = "Please upload an image.";
        return;
    }

    const formData = new FormData();
    formData.append('image', fileInput.files[0]);

    try {
        const response = await fetch('http://localhost:5000/count', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || "Server error");
        }

        document.getElementById('carCount').innerText = data.counts.cars;
        document.getElementById('motoCount').innerText = data.counts.motorcycles;
        document.getElementById('heavyCount').innerText = data.counts.heavy_vehicles;
        document.getElementById('totalCount').innerText = data.counts.total;
        
        document.getElementById('resultImage').src = "data:image/jpeg;base64," + data.image;
        resultsSection.classList.remove('results-hidden');

        if (data.counts.total === 0) {
            errorDiv.innerText = "No vehicles detected in this image.";
        }

    } catch (error) {
        errorDiv.innerText = error.message;
    }
}