
function initmap() {
    
    var location = new google.maps.LatLng(53.349562,-6.278198);
    
    var mapOptions = {
        zoom: 15,
        center: location,
        streetViewControl: false,
        scaleControl: true,
        zoomControl: true,
        zoomControlOptions: {
            position: google.maps.ControlPosition.TOP_CENTER,
            style: google.maps.ZoomControlStyle.LARGE
        },
        draggableCursor:'crosshair'
    };
    var map = new google.maps.Map(document.getElementById('map-canvas'),mapOptions);
    
    var marker = new google.maps.Marker({
        position: location, 
        map: map,
        icon: {
            path: google.maps.SymbolPath.CIRCLE,
            fillColor: '#FFFFFF',
            fillOpacity: 1,
            strokeColor: '#00FF00',
            strokeWeight: 3,
            scale: 6
        }
    });
    
    google.maps.event.addListener(marker, 'mouseover', function(e) {
        this.setIcon({
            path: google.maps.SymbolPath.CIRCLE,
            fillColor: '#FFFFFF',
            fillOpacity: 1,
            strokeColor: '#FF0000',
            strokeWeight: 3,
            scale: 6
        });
    });
    
    google.maps.event.addListener(marker, 'mouseout', function(e) {
        this.setIcon({
            path: google.maps.SymbolPath.CIRCLE,
            fillColor: '#FFFFFF',
            fillOpacity: 1,
            strokeColor: '#00FF00',
            strokeWeight: 3,
            scale: 6
        });
    });
}


