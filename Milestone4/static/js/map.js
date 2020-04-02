// Map js
let mapTileLayers = L.tileLayer("http://services.arcgisonline.com/arcgis/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}", {
    attribution: "Powered by <a href='https://developers.arcgis.com/terms/attribution/' target='_blank' rel='noopener'>Esri</a>"
});

// Generating the map
let map = L.map("map", {
    layers: [mapTileLayers],
    center: [52.257307, -7.134089],
    zoom: 15
});
let mapOverlay = L.tileLayer("http://services.arcgisonline.com/arcgis/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}");
mapOverlay.bringToFront().addTo(map).setZIndex(9);

// Creating the custom map Marker, using the Brand Logo and positioning same on the map
let logoMarker = L.icon({
    iconUrl: 'https://raw.githubusercontent.com/auxfuse/Milestone4/carousel-map-about/Milestone4/static/img/mapPinlogo.png',
    iconSize: [103, 50],
    iconAnchor: [51.5, 25]
});

let myMarker = L.marker([52.257307, -7.134089], {icon: logoMarker}).addTo(map);