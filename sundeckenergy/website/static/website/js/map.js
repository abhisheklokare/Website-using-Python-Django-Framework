var map;
var markers = [];
var infoWindow;
var service;
var currentCoords = {};

function displayLocation(position) {
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
    var accuracy = position.coords.accuracy;
    showMap(position.coords);
}

function showMap(coords) {
    currentCoords.latitude = coords.latitude;
    currentCoords.longitude = coords.longitude;

    var googleLatLong = new google.maps.LatLng(coords.latitude, coords.longitude);

    var mapOptions = {
        zoom: 11,
        center: googleLatLong,
        mapTypeId: google.maps.MapTypeId.SATELITE
    };

    var mapDiv = document.getElementById('map');
    map = new google.maps.Map(mapDiv, mapOptions);
    infoWindow = new google.maps.InfoWindow();
    service = new google.maps.places.PlacesService(map);

    google.maps.event.addListener(map, "click", function (event) {
        var latitude = event.latLng.lat();
        var longitude = event.latLng.lng();
        currentCoords.latitude = coords.latitude;
        currentCoords.longitude = coords.longitude;

        var pLocation = document.getElementById("location");
        // pLocation.innerHTML += (latitude + ", " + longitude + "</br>");
        map.panTo(event.latLng);

        // createMarker(event.latLng);
    });

    showForm();
}

function makePlacesRequest(lat, lng) {
    var query = document.getElementById("query").value;
    if (query) {
        var placesRequest = {
            location: new google.maps.LatLng(lat, lng),
            radius: 5000,
            keyword: query
        };

        service.nearbySearch(placesRequest, function (results, status) {
            if (status == google.maps.places.PlacesServiceStatus.OK) {
                results.forEach(function (place) {
                    createMarker(place);
                });
            }
        })

    }
}

// //Showing marker based on current location
// function createMarker(latLng) {
//     var markerOptions = {
//         position: latLng,
//         map: map,
//         clickable: true
//     };

//     var marker = new google.maps.Marker(markerOptions);
//     markers.push(marker);

//     google.maps.event.addListener(marker, "click", function (event) {
//         infoWindow.setContent("Location:" + event.latLng.lat().toFixed(2) + ", " + event.latLng.lng().toFixed(2));
//         infoWindow.open(map, marker);
//     })
// }

// Showing marker based on searched location
function createMarker(place) {
    var markerOptions = {
        position: place.geometry.location,
        map: map,
        clickable: true
    };

    var marker = new google.maps.Marker(markerOptions);
    markers.push(marker);

    google.maps.event.addListener(marker, "click", function (place, marker) {
        return function() {
            if (place.vicinity) {
                infoWindow.setContent(place.name + "</br>" + place.vicinity);
            } else {
                infoWindow.setContent(place.name);
            }

            infoWindow.open(map, marker);
        };
    }(place, marker));
}

function clearMarkers() {
    markers.forEach( function(marker) {marker.setMap(null); });
    markers = [];
}

function showForm() {
    var searchForm = document.getElementById("gform");
    searchForm.style.visibility = "visible";

    var searchButton = document.getElementById("locate");
    searchButton.onclick = function (e) {
        e.preventDefault();
        clearMarkers();
        makePlacesRequest(currentCoords.latitude, currentCoords.longitude);
    }
}

function displayErrors(error) {
    var errors = ["Unknown Error", "Permission Denied by user", "Location not availble"];
    var message = errors[error.code];
    console.warn("Error in getting your location:" + message, error.message);
}

var options = {
    enableHighAccuracy: true,
    timeout: 5000,
    maximumAge: 0
};

window.onload = function () {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(displayLocation, displayErrors);
    } else {
        alert("This browser does  not support geolocation service");
    }
}