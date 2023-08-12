const Check = (cssSelector) => {
    let inputArray = document.querySelectorAll(cssSelector);
    for (input of inputArray) {
        if (input.value === "") {
            // block form sending info to server 
            event.preventDefault();
        };
    };
};

const DeleteCheck = (element) => {
    if (confirm("是否刪除留言")) {
        let comment_id = element.getAttribute("id");

        fetch("/deleteMessage", {
            method : "POST",
            headers: {"Content-Type": "application/json"},
            body : JSON.stringify({
                comment_id : comment_id
            })
        })
        .then(DeleteCheck(response)
            //pass
        )}else{
        event.preventDefault();
    };
};