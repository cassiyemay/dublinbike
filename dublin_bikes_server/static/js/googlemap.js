

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

    console.log("create map");
    //in parameter - stationCoord(object, structure is 0:"-6.30395")
    setmarker(map);
    
};

function setmarker(map) {
    
    stationCoord = getStationCoord();
    console.log(stationCoord);
    
    var Markers = [];
    
    //set marker for all
    for(i in stationCoord.latitude) {
        
        console.log(stationCoord.longitude[i]);
        var lo = new google.maps.LatLng(stationCoord.longitude[i],stationCoord.longitude[i]);
        
        var marker = new google.maps.Marker({
            position: lo, 
            map: map,
            icon: {
                path: google.maps.SymbolPath.CIRCLE,
                fillColor: '#FFFFFF',
                fillOpacity: 1,
                strokeColor: '#87fd49',
                strokeWeight: 3,
                scale: 6}
        });
        
        Markers.push(marker);
    };

};