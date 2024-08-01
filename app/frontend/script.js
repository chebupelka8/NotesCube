"use strict";


import { UserRepository } from "./src/user_repository.js";
import { HTMLManager } from "./src/html_manager.js";


const searchUserInput = document.getElementById("search-users");

document.getElementById("search").addEventListener("click", function() {
    if (searchUserInput.value.trim().length > 0) {
        UserRepository.searchUser(searchUserInput.value).then(function(response) {
            HTMLManager.showReceivedUsers(response["found"]);
        });
    }
})