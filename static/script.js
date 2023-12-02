document.addEventListener('DOMContentLoaded', function() {
    // Fetch the list of documents and populate the dropdown
    fetch('/list_documents')
        .then(response => response.json())
        .then(files => {
            const selectElement = document.getElementById('document-name');
            files.forEach(file => {
                const option = document.createElement('option');
                option.value = option.textContent = file;
                selectElement.appendChild(option);
            });
        });
    document.getElementById('load-form').addEventListener('submit', function(e) {
        e.preventDefault();
        var documentName = document.getElementById('document-name').value;
        startProgressBar();
        fetch('/load_vectorstore', {
            method: 'POST',
            body: new URLSearchParams({
                'document_name': documentName
            })
        })
        .finally(() => {
            stopProgressBar();
        })
        .then(response => response.json())
        .then(data => {
            // Assuming data is an object or array, format it as a JSON string
            document.getElementById('response').textContent = JSON.stringify(data, null, 2);
        });
    });

    document.getElementById('query-form').addEventListener('submit', function(e) {
        e.preventDefault();
        var prompt = document.getElementById('prompt').value;
        startProgressBar();
        fetch('/query', {
            method: 'POST',
            body: new URLSearchParams({
                'prompt': prompt
            })
        })
        .finally(() => {
            stopProgressBar();
        })
        .then(response => response.json())
        .then(data => {
            const chatInterface = document.getElementById('chat-interface');
            const message = document.createElement('div');
            message.classList.add('chat-message', 'system-message');
            message.textContent = JSON.stringify(data, null, 2);
            chatInterface.appendChild(message);
            chatInterface.scrollTop = chatInterface.scrollHeight; // Scroll to the bottom
        });
    });
});

function startProgressBar() {
    var progressBar = document.getElementById('progress-bar');
    progressBar.style.width = '100%';
}

function stopProgressBar() {
    var progressBar = document.getElementById('progress-bar');
    progressBar.style.width = '0%';
}
