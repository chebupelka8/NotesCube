"use strict";

import { Requests } from "./request.js";
import { Path } from "./path.js";


export class UserRepository extends Requests {
    static prefix = "http://localhost:8080"

    static async searchUser(query) {
        const url = Path.mergeUrl(UserRepository.prefix, `/users/search?query=${query}`);
        console.log(url);
        return await UserRepository.requestJson(url);
    }
}
