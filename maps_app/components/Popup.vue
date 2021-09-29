<template>

  <section class="p-2 bg-gray-100 h-screen overflow-hidden">
    <p v-if="date!==' '" class="w-full text-center pt-6 px-20 text-3xl font-semibold">{{ name }}, {{ date }}</p>
    <p v-else class="w-full text-center pt-6 px-20 text-3xl font-semibold">{{ name }}</p>

    <p v-if="pictures && pictures.length > 1" class="px-2 pt-6 pb-2">Images :</p>
    <!-- <img v-for="(picture, index) in pictures" :key="index" :src="picture.path_directory+'/'+picture.filename" :alt="picture.filename"> -->
    <div v-if="pictures && pictures.length > 1" class="wrapper w-full h-5/6 overflow-y-scroll overflow-x-hidden flex flex-row flex-wrap">
      <img v-for="(picture, index) in pictures" :key="index" :src="require(`~/assets/${picture.filename}`)" :alt="picture.filename" v-on:click="emitToParent($event,picture, index)" class="picture block w-1/2 p-2">
    </div>
  </section>

</template>

<script>
  import VueSlickCarousel from 'vue-slick-carousel'
  
  export default {
    name: "Popup",
    props: ["id", "name", "date", "pictures"],
    data: function () {
      return {
      }
    },
    components: { 
      VueSlickCarousel
    }, 
    methods: {
      /**
       * Emit to parent when picture is clicked
       */
      emitToParent (event, picture, index) {
        this.$emit('clicked', {
          event: event,
          displaySlider: true,
          pictureClicked: picture,
          index: index
        });
      }
    }
  }
</script>

<style type="scss" scoped>
  .sliders-pic {
    margin-left: -80%;
  }
</style>

