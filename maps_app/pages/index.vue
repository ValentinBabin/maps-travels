<template>
  <section>
    <div class="map">
      <client-only>
        <Map/>
      </client-only>
    </div>
    
    <div class="footer">
      <Footer/>
    </div>
  </section>
</template>

<script lang="ts">

import Vue from 'vue';

export default Vue.extend({})

</script>

<style type="scss" scoped>
  section{
    position: relative;
  }
  .map{
    z-index: 1;
  }
  .footer {
    z-index: 400;
    position: absolute;
    bottom: 0;
    left: 0;
    
    /* padding: 20px; */
  }
</style>
