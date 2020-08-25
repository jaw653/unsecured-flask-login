document.getElementById("btn").addEventListener("click", () => {
    // The URL to which our POST is being sent (this machine's IP)
    const serverURL = "http://0.0.0.0:5000/";

    // JS object containing username and password
    var msg = {
        "username": document.getElementById("user").value,
        "password": document.getElementById("pass").value
    };

    // Object in JSON form for sending
    var stringified_body = JSON.stringify(msg);

    // Fetch() API is used in JS to send HTTP requests
    fetch(serverURL, {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: stringified_body
    });
});
