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
        var collectionNameLoad = document.getElementById('collection-name-load').value;
        fetch('/load_vectorstore', {
            method: 'POST',
            body: new URLSearchParams({
                'document_name': documentName,
                'collection_name': collectionNameLoad
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
        appendUserMessage(prompt); // Append the user's message to the chat
        startProgressBar();
        var collectionNameQuery = document.getElementById('collection-name-query').value;
        fetch('/query', {
            method: 'POST',
            body: new URLSearchParams({
                'prompt': prompt,
                'collection_name': collectionNameQuery
            })
        })
        .finally(() => {
            stopProgressBar();
        })
        .then(response => response.json())
        .then(data => {
            appendSystemMessage(JSON.stringify(data, null, 2)); // Append the system's response to the chat
        });
    });

    function appendUserMessage(text) {
        const chatInterface = document.getElementById('chat-interface');
        const message = document.createElement('div');
        message.classList.add('chat-message', 'user-message');
        message.textContent = "User: " + text;
        chatInterface.appendChild(message);
    }

    function appendSystemMessage(text) {
        const chatInterface = document.getElementById('chat-interface');
        const message = document.createElement('div');
        message.classList.add('chat-message', 'system-message');
        // Format the text to display special characters properly as HTML
        const formattedText = text
            .replace(/\n/g, '<br>')
            .replace(/\r/g, '') // Carriage returns are not needed in HTML, remove them
            .replace(/\t/g, '&nbsp;&nbsp;&nbsp;&nbsp;'); // Replace each tab with 4 non-breaking spaces
        message.innerHTML = "Assistant: " + formattedText; // Use innerHTML to parse the HTML tags
        chatInterface.appendChild(message);
        chatInterface.scrollTop = chatInterface.scrollHeight; // Scroll to the bottom
    }
});

function startProgressBar() {
    var progressBar = document.getElementById('progress-bar');
    progressBar.style.width = '100%';
}

function stopProgressBar() {
    var progressBar = document.getElementById('progress-bar');
    progressBar.style.width = '0%';
}
