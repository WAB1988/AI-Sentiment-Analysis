async function analyzeSentiment() {
    const url = document.getElementById('urlInput').value;
    const query = document.getElementById('queryInput').value;
    
    if (!url || !query) {
        alert('Please enter both URL and analysis query');
        return;
    }

    // Show loading spinner and disable button
    const analyzeBtn = document.getElementById('analyzeBtn');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const resultSection = document.getElementById('resultSection');
    const analysisResult = document.getElementById('analysisResult');

    analyzeBtn.disabled = true;
    loadingSpinner.style.display = 'block';
    resultSection.style.display = 'none';

    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url, query })
        });

        const data = await response.json();
        
        if (data.success) {
            analysisResult.textContent = data.analysis;
            resultSection.style.display = 'block';
        } else {
            alert('Error: ' + data.error);
        }
    } catch (error) {
        alert('Error: ' + error.message);
    } finally {
        analyzeBtn.disabled = false;
        loadingSpinner.style.display = 'none';
    }
}
