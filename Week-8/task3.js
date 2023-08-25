let googleUrl = "https://www.google.com";
let testUrl = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";

fetch(googleUrl, {
    method : "DELETE",
    "Content-type" : "application/json"
})
    .then(response => {
        return response.headers;
    })
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.log(error);
    });

fetch(testUrl)
    .then(res => {
        return res.headers;
    })
    .then(data => {
        console.log(data);
    })
    .catch(error => {
        console.log(error);
    })
