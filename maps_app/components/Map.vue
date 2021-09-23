<template>

  <div class="map">
    <l-map 
      :zoom="zoom"
      :center="center"
      @update:zoom="zoomUpdated"
      @update:center="centerUpdated">
      <l-tile-layer :url="url" :attribution="attribution" :tileSize="tileSize" :options="{ zoomOffset: -1, maxZoom:maxZoom }"></l-tile-layer>
      <!-- Limoges -->
      <l-marker :lat-lng="latLng(45.833619, 1.261105)">
        <l-icon icon-url="https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png" />
      </l-marker>
      <!-- Fleix -->
      <l-marker :lat-lng="latLng(46.5549, 0.7461)">
        <l-icon icon-url="https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png" />
      </l-marker>

      <!-- Custom -->
      <l-marker v-for="city in cities" :key="city.id" :lat-lng="latLng(city.lat, city.lng)" v-on:click="onMarkerClick(city.id, city.name, city.date)">
        <l-icon icon-url="https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-blue.png" />
      </l-marker>
    </l-map>

    <div v-if="cityId && cityName && cityDate" class="popup h-screen w-1/3">
      <Popup :id="cityId" :name="cityName" :date="cityDate" />
    </div>
  </div>

</template>

<script>
  /* eslint-disable no-undef */
  let Vue2Leaflet = {}
  if (process.client)
    Vue2Leaflet = require('vue2-leaflet')
  export default {
    name: "Map",
    props: [],
    data: function () {
      return {
        center: L.latLng(45.833619, 1.261105),
        url: 'https://api.mapbox.com/styles/v1/mapbox/streets-v11/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoidmFsZW50aWluIiwiYSI6ImNrb2I0MG52bDJ2dnAycGxwNGppNGl6dmgifQ.UiZb90834w5Nx4tM6mly1w',
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',    
        zoom: 7,
        iconSize: [25, 41],
        tileSize:512,
        maxZoom:18,
        bounds: null,
        cities: null,
        cityId: null,
        cityName: null,
        cityDate: null
      }
    },
    components: {
      'l-map': Vue2Leaflet.LMap,
      'l-tile-layer': Vue2Leaflet.LTileLayer,
      'l-marker': Vue2Leaflet.LMarker,
      'l-icon': Vue2Leaflet.LIcon
    }, 
    methods: {
      latLng: function (lat, lng) {
        return L.latLng(lat, lng);
      },
      zoomUpdated (zoom) {
        this.zoom = zoom;
      },
      centerUpdated (center) {
        this.center = center;
      },
      boundsUpdated (bounds) {
        this.bounds = bounds;
      },
      onMarkerClick: function (id, name, date) {
        this.cityId=id;
        this.cityName=name;
        this.cityDate=date;
      },
    },
    async fetch() {
      const cities = await this.$axios.$get('https://api.valentinbabin.fr/api_cities/view.php')
      this.cities = cities;
    }
  }
</script>

<style type="scss" scoped>
  .map {
    height: 100vh;
  }
  .popup {
    z-index: 500;
    position: absolute;
    top: 0;
    right: 0;
  }
</style>
