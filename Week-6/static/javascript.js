const Check = () => {
    let// 
    nameInput = document.querySelector(".name-input"),
    accountInput = document.querySelector(".account-input"),
    passwordInput = document.querySelector(".password-input");

    if ( nameInput.value === "" || accountInput.value === "" || passwordInput === "" ) {
        // block form sending info to server 
        event.preventDefault();
    }
};
