const Check = (cssSelector) => {
    let inputArray = document.querySelectorAll(cssSelector);
    for (input of inputArray) {
        if (input.value === "") {
            // block form sending info to server 
            event.preventDefault();
        };
    };
};

const DeleteCheck = async (element) => {
    if (confirm("是否刪除留言")) {
        let comment_id = element.getAttribute("id");

        let post = await fetch("/deleteMessage", {
            method : "POST",
            headers: {"Content-Type": "application/json"},
            body : JSON.stringify({
                comment_id : comment_id
            })
        });
        let response = await post.json(); 
        // after fetch succeed, must to be ended with using json() or text() to parse response from fetch;
        // otherwise, the program after fetch would not run.

        }else{
        event.preventDefault();
    };
};

const SearchMember =  async () => {
    let searchUsername = document.querySelector(".search-input").value;

    let search = await fetch("/api/member?" + new URLSearchParams({
        username : searchUsername
    }));

    let response = await search.json();
    let result = await response['data'];

    let searchResult = document.querySelector(".search-result");
    searchResult.innerHTML = result['name'] + "(" + result['username'] + ")";
    searchResult.style.visibility = "visible";
};