/// <reference path="../references.ts" />

module Demo.CoworkingMap {

    export class CoworkingMapPresenter {

        private map: google.maps.Map;

        private infoTemplate: string = null; 
        private openedInfo: google.maps.InfoWindow = null;

        initialize(): void {

            var mapCanvas = document.getElementById("map-canvas");

            var mapOptions: google.maps.MapOptions = {
                mapTypeId: <google.maps.MapTypeId>google.maps.MapTypeId.ROADMAP,
                center: new google.maps.LatLng(9.51202, 100.01359),
                zoom: 12
            };

            this.map = new google.maps.Map(mapCanvas, mapOptions);
        }

        addCoworking(coworking: CoworkingItem): void {
            
            if (!coworking) {
                throw new Error("coworking is null.");
            }
            
            var markerOptions: google.maps.MarkerOptions = {
                position: new google.maps.LatLng(coworking.location[0], coworking.location[1]),
                title: coworking.name,
                icon: coworking.icon
            }

            var marker = new google.maps.Marker(markerOptions);

            var infoWindowOptions: google.maps.InfoWindowOptions = {
                content: this.getInfoContent(coworking)
            };

            google.maps.event.addListener(marker, 'click', () => {
                this.showInfo(marker, infoWindowOptions);
            });

            marker.setMap(this.map);
        }

        private getInfoContent(coworking: CoworkingItem): any {

            if (!this.infoTemplate) {
                var templateObject = <HTMLScriptElement>document.getElementById("coworkingInfoTemplate");
                this.infoTemplate = templateObject.innerHTML;
                Mustache.parse(this.infoTemplate);
            }

            return Mustache.render(this.infoTemplate, coworking);
        }
        
        private showInfo(marker: google.maps.Marker, infoWindowOptions: google.maps.InfoWindowOptions): void {
            
            if (this.openedInfo) {
                this.openedInfo.close();
                this.openedInfo = null;
            }
            
            var infoWindow = new google.maps.InfoWindow(infoWindowOptions);

            infoWindow.open(this.map, marker);
            this.openedInfo = infoWindow;
        }
    }
}
