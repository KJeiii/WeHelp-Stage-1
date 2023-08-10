const Check = (cssSelector) => {
    let inputArray = document.querySelectorAll(cssSelector);
    for (input of inputArray) {
        if (input.value === "") {
            // block form sending info to server 
            event.preventDefault();
        };
    };
};

const DeleteCheck = () => {
    if (confirm("是否刪除留言")) {
        //pass
    }else{
        event.preventDefault();
    };
};