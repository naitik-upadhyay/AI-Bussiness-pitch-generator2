async function generatePitch() {
    const idea = document.getElementById('idea').value;
    const problem = document.getElementById('problem').value;
    const audience = document.getElementById('audience').value;
    const features = document.getElementById('features').value;

    const loader = document.getElementById('loader');
    const resultDiv = document.getElementById('result');

    resultDiv.innerHTML = '';
    loader.classList.remove('hidden');

    try {
        const response = await fetch('http://localhost:5000/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ idea, problem, audience, features })
        });

        const data = await response.json();
        loader.classList.add('hidden');
        resultDiv.innerHTML = data.output;
    } catch (error) {
        loader.classList.add('hidden');
        resultDiv.innerHTML = "<p style='color:red;'>❌ Failed to generate pitch. Please try again.</p>";
    }
}
