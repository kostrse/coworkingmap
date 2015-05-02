/// <reference path="../references.ts" />

module Demo.CoworkingMap {

    export interface CoworkingItem {
        name: string;
        location: [number, number];
        locationDescr: string;
        icon: string;
        image: string;
        closed: boolean;
    }
}
