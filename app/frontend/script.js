"use strict";


import { UserRepository } from "./src/user_repository.js";


const searchUserInput = document.getElementById("search-users");
document.getElementById("search").addEventListener("click", function() {
    if (searchUserInput.value.trim().length > 0) {
        UserRepository.searchUser(searchUserInput.value).then(response => console.log(response));
    }
})