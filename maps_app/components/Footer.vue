<template>

  <footer class="leaflet-container">
    <div class="leaflet-control-attribution leaflet-control">
      <span>v2.0</span>
      <span>|</span>
      <span><NuxtLink to="/changelog">changelog</NuxtLink></span>
      <span>|</span>
      <span>© <a href="https://valentinbabin.fr" target="_blank"> Valentin Babin </a> - 2021</span>
    </div>
  </footer>

</template>

<script>
  export default {
    name: "Footer",
    props: [],
    data: function () {
      return { }
    },
    components: { }, 
    methods: { }
  }
</script>

<style type="scss" scoped>

  span {
    font-size: 11px;
    font-family: "Helvetica Neue", Arial, Helvetica, sans-serif;
    line-height: 1.5;
    font-weight: 400;
    font-stretch: 100%;
    font-style:normal;
    font-variant-caps:normal;
    font-variant-east-asian:normal;
    font-variant-ligatures:normal;
    font-variant-numeric:normal;
  }
  
</style>

