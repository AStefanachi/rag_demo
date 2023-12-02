document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('load-form').addEventListener('submit', function(e) {
        e.preventDefault();
        var documentName = document.getElementById('document-name').value;
        var collectionName = document.getElementById('collection-name').value;
        fetch('/load_vectorstore', {
            method: 'POST',
            body: new URLSearchParams({
                'document_name': documentName,
                'collection_name': collectionName
            })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('response').textContent = JSON.stringify(data);
        });
    });

    document.getElementById('query-form').addEventListener('submit', function(e) {
        e.preventDefault();
        var prompt = document.getElementById('prompt').value;
        fetch('/query', {
            method: 'POST',
            body: new URLSearchParams({
                'prompt': prompt
            })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('response').textContent = JSON.stringify(data);
        });
    });
});
