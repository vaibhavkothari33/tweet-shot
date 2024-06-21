// Example JavaScript for form submission and handling

document.getElementById('fetchForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var tweetUrl = document.getElementById('tweetUrl').value;

    fetch('/fetch_tweet', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'tweetUrl=' + encodeURIComponent(tweetUrl)
    })
    .then(response => response.json())
    .then(data => {
        // Update DOM with tweet details
        var tweetDetails = document.getElementById('tweetDetails');
        tweetDetails.innerHTML = `
            <h2>${data.author}</h2>
            <img src="${data.author_image}" alt="Author Image">
            <p>${data.text}</p>
            <p>Likes: ${data.likes}</p>
            <p>Retweets: ${data.retweets}</p>
        `;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
