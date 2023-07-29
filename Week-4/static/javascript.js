const CheckAgreement = () => {
    let checkbox = document.querySelector(".checkbox");
    if ( checkbox.checked !== true ) {

        // block form sending info to server 
        event.preventDefault();
        alert("Please check the checkbox first");
    }
};

const CheckInt = () => {
    event.preventDefault();
    let numInputElement = document.querySelector(".input-num");
    let inputNum = Number(numInputElement.value);
    if ( !Number.isInteger(inputNum) || inputNum <= 0) {
        alert("Please enter a positive integer.");
    }else{
        let originUrl = window.location.origin;
        let squareUrl = originUrl + "/square/" + numInputElement.value;
        window.location.replace(squareUrl);
    };
}