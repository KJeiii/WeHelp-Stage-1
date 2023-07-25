let submitBtn = document.querySelector(".submit-btn");
let checkbox = document.querySelector(".checkbox");
let formLoginDiv = document.querySelector(".login")
let accountInput = document.querySelector(".account-input")
let passwordInput = document.querySelector(".password-input")

const CheckAgreement = () => {
    if ( checkbox.checked !== true ) {
        alert("Please check the checkbox first");

        // clear user info in the url
        accountInput.value = "";
        passwordInput.value = "";

        // clear the action and method attributes,
        // otherwise using browser next page or previos page button 
        // could pass verification without check agreement

        formLoginDiv.setAttribute("action","");
        formLoginDiv.setAttribute("method", "");
    }else{
        formLoginDiv.setAttribute("action","/signin");
        formLoginDiv.setAttribute("method", "post");
    }
};