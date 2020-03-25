// Map js
let mapTileLayers = L.tileLayer("http://services.arcgisonline.com/arcgis/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}", {
    attribution: "Powered by <a href='https://developers.arcgis.com/terms/attribution/' target='_blank' rel='noopener'>Esri</a>"
});
let map = L.map("map", {
    layers: [mapTileLayers],
    center: [23.5, 12],
    zoom: 2
});
let myMarker = L.marker([-22.951993, -43.210439]).addTo(map);