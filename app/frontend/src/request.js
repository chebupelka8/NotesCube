"use strict";


export class Requests {
    static async request(url) {
        return await fetch(url);
    }

    static async requestJson(url) {
        const response = await Requests.request(url);
        return await response.json();
    }
}
