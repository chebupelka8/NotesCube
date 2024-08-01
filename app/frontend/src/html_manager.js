"use strict";


export class HTMLManager {

    static showReceivedUsers(users) {
        if (users.length === 0) return;

        const appendLabelsToElementFromObject = function(user, keys, element) {
            keys.forEach(function(entry) {
                const label = document.createElement("label");
                label.classList.add(entry);
                label.appendChild(document.createTextNode(user[entry]));
                element.appendChild(label);
            });
        }

        users.forEach(function(entry) {
            const containerDiv = document.createElement("div");
            containerDiv.classList.add("user");
    
            appendLabelsToElementFromObject(
                entry,
                ["first_name", "last_name"],
                containerDiv
            );

            document.getElementById("users-preview").appendChild(containerDiv);
        });
    }
    
}
