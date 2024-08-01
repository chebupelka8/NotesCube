"use strict";

import { Requests } from "./request.js";
import { Path } from "./path.js";


export class UserRepository extends Requests {
    static prefix = "http://localhost:8080"

    static async searchUser(query) {
        const url = Path.mergeUrl(UserRepository.prefix, "/users/search");
        return await UserRepository.requestJson(Path.addQueryParams(url, {"query": query}));
    }

    static async getUserById(id) {
        const url = Path.mergeUrl(UserRepository.prefix, `/users/${id}`);
        return await UserRepository.requestJson(url);
    }
}
