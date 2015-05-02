/// <reference path="references.ts" />

module Demo.CoworkingMap {

    export class Application {

        private mapPresenter: CoworkingMapPresenter;

        constructor() {
            this.mapPresenter = new CoworkingMapPresenter();
        }

        initialize(): void {

            // Initializing the map.
            this.mapPresenter.initialize();

            // Adding coworkings from the list.
            knownCoworkings.forEach(coworking => {
               this.mapPresenter.addCoworking(coworking); 
            });
        }
    }
}
