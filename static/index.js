let mymap = L.map("mapid").setView([38.5449, -121.7405], 13);
L.tileLayer(
  "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
  {
    attribution:
      'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: "mapbox/streets-v11",
    tileSize: 512,
    zoomOffset: -1,
    accessToken:
      "pk.eyJ1Ijoic2pjdHJhIiwiYSI6ImNrM2dsdXd1bjAzNngzY21zcWxxMDA2dXoifQ.EqzC2hpVP7tiXrDgXXNrvQ",
  }
).addTo(mymap);
