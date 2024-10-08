"use strict";

import { UserRepository } from "./src/user_repository.js";
import { HTMLManager } from "./src/html_manager.js";


const searchUserInput = document.getElementById("search-users");
const usersPreview = document.getElementById("users-preview");

document.getElementById("search").addEventListener("click", function() {
    usersPreview.innerHTML = ""; // clear userPreview

    if (searchUserInput.value.trim().length > 0) {
        UserRepository.searchUser(searchUserInput.value).then(function(response) {
            console.log(response["found"]);
            HTMLManager.showReceivedUsers(response["found"]);
        });
    }
});