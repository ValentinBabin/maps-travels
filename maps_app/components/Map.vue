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

      <!-- Custom -->
      <l-marker v-for="city in cities" :key="city.id" :lat-lng="latLng(city.lat, city.lng)" v-on:click="onMarkerClick(city.id, city.name, city.date)">
        <l-icon icon-url="https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-blue.png" />
      </l-marker>
    </l-map>

    <div v-if="cityId && cityName && cityDate" class="popup h-screen w-full md:w-2/5 overflow-hidden">
      <p class="absolute my-1 mx-3 select-none cursor-pointer hover:underline text-xs" v-on:click="closePopup()">fermer</p>
      <Popup :id="cityId" :name="cityName" :date="cityDate" :pictures="picturesTab" @clicked="displaySlider" />
    </div>

    <div v-if="showSlider" class="sliders-pic absolute left-0 top-0 h-screen">
      <p class="closing absolute right-0 my-1 mx-3 select-none cursor-pointer hover:underline text-xs" v-on:click="closeSlider()">fermer</p>
      <VueSlickCarousel ref="carousel" :arrows="true" :dots="true" :slidesToShow="1" @init="onInitCarousel(indexSlide)">
        <img v-for="(picture, index) in picturesTab" :key="index" :src="'medias/'+picture.filename" :alt="picture.filename">
        <template #prevArrow="">
          <div class="custom-arrow cursor-pointer">
            <font-awesome-icon icon="arrow-left" />
          </div>
        </template>
        <template #nextArrow="">
          <div class="custom-arrow cursor-pointer">
            <font-awesome-icon icon="arrow-right" />
          </div>
        </template>
      </VueSlickCarousel>
    </div>
  </div>

</template>

<script>
  import Vue from 'vue';
  /* eslint-disable no-undef */
  let Vue2Leaflet = {}
  if (process.client)
    Vue2Leaflet = require('vue2-leaflet')

  import VueSlickCarousel from 'vue-slick-carousel';
  import 'vue-slick-carousel/dist/vue-slick-carousel.css';
  // import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css';
  import { library } from '@fortawesome/fontawesome-svg-core'
  import { faArrowLeft, faArrowRight } from '@fortawesome/free-solid-svg-icons'
  import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

  library.add(faArrowLeft);
  library.add(faArrowRight);

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
        cityDate: null,
        picturesTab: null,
        showSlider: false,
        indexSlide:null,
      }
    },
    components: {
      'l-map': Vue2Leaflet.LMap,
      'l-tile-layer': Vue2Leaflet.LTileLayer,
      'l-marker': Vue2Leaflet.LMarker,
      'l-icon': Vue2Leaflet.LIcon,
      VueSlickCarousel,
      'font-awesome-icon': FontAwesomeIcon
    }, 
    methods: {
      // Events when map update
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
      onMarkerClick (id, name, date) {
        this.cityId=id;
        this.cityName=name;
        this.cityDate=date;
        this.getPictures(id).then( (res)=>{
          this.picturesTab = res;
        });
      },
      // Closing methods
      closePopup (){
        this.cityId=null;
        this.cityName=null;
        this.cityDate=null;
        this.picturesTab=null;
      },
      closeSlider (){
        this.showSlider=false;
      },
      /**
       * Get pictures form WEB API
       */
      async getPictures (id){
        return await this.$axios.$get(`https://api.valentinbabin.fr/api_cities/view_media.php?id=${id}`);
      },
      displaySlider (value) {
        this.showSlider=value.displaySlider;
        this.indexSlide=value.index;
      },
      onInitCarousel(index) {
        setTimeout(() => {
          this.$refs.carousel.goTo(index);
        }, 500);
      },
    },
    async fetch() {
      const cities = await this.$axios.$get('https://api.valentinbabin.fr/api_cities/view.php')
      this.cities = cities;
    }
  }
</script>

<style type="scss">
  .map {
    height: 100vh;
  }
  .popup {
    z-index: 1000;
    position: absolute;
    top: 0;
    right: 0;
    height: 100vh;
  }
  .closing{
    z-index: 1000;
  }
  .sliders-pic{
    z-index: 1001;
    width: 100%;
    background-color: rgba(209, 213, 219, 0.65);
  }
  .slick-slider{
    width: 100%;
    height: 100%;
    overflow-x: hidden;
  }
  .slick-list,
  .slick-track,
  .slick-slide{
    width: 100%;
    height: 100%;
  }
  .slick-slide div{
    width: 100%;
    height: 100%;
    padding: 50px 75px 100px 75px;
  }
  @media (max-width: 769px){
    .slick-slide div{
      display: flex;
      align-items: center;
      justify-content: center;
    }
  }

  .slick-slide div img{
    width: auto !important;
    height: 100%;
    display: block !important;
    margin: 0 auto;
  }
  @media (max-width: 769px){
    .slick-slide div img{
      width: 100% !important;
      height: auto;
    }
  }

  .slick-dots{
    position: absolute;
    left: 0;
    bottom: 20px;
    width: 100%;
    display: flex !important;
    flex-direction: row;
    justify-content: center;
  }
  .slick-dots li{
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background-color: #6b7280;
    margin: 0 10px;
  }
  .slick-dots li.slick-active{
    background-color: #1f2937;
  }
  .slick-dots li button{
    display: none;
  }
  .slick-prev{
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    left: 10px;
    z-index: 1001;
  }
  .slick-next{
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    right: 10px;
    z-index: 1001;
  }
</style>
