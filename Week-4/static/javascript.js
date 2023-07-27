const CheckAgreement = () => {
    let checkbox = document.querySelector(".checkbox");
    if ( checkbox.checked !== true ) {

        // block form sending info to server 
        event.preventDefault();
        alert("Please check the checkbox first");
    }
};

const CheckInt = () => {
    let numInputElement = document.querySelector(".input-num")
    let inputNum = Number(numInputElement.value);
    if ( !Number.isInteger(inputNum) || inputNum <= 0) {
        event.preventDefault();
        alert("Please enter a positive integer.");
    };

}