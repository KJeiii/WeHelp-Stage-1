let submitBtn = document.querySelector(".submit-btn");
let checkbox = document.querySelector(".checkbox");
let formLoginDiv = document.querySelector(".login")
let accountInput = document.querySelector(".account-input")
let passwordInput = document.querySelector(".password-input")

const CheckAgreement = () => {
    if ( checkbox.checked !== true ) {

        // block form sending info to server 
        event.preventDefault();
        alert("Please check the checkbox first");
    }
};