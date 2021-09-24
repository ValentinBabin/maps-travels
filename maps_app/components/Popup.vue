<template>

  <section class="p-2 bg-gray-100 h-screen overflow-hidden">
    <p class="w-full text-center pt-6 px-20 text-3xl font-semibold">{{ name }}, {{ date }}</p>
    <p class="px-2 pt-6 pb-2">Images :</p>
    <!-- {{pictures}} -->
    <!-- <img v-for="(picture, index) in pictures" :key="index" :src="picture.path_directory+'/'+picture.filename" :alt="picture.filename"> -->
    <div class="wrapper w-full h-5/6 overflow-y-scroll overflow-x-hidden flex flex-row flex-wrap">
        <img v-for="(picture, index) in pictures" :key="index" :src="require(`~/assets/${picture.filename}`)" :alt="picture.filename" class="picture block w-1/2 p-2">
    </div>
  </section>

</template>

<script>
  export default {
    name: "Popup",
    props: ["id", "name", "date", "pictures"],
    data: function () {
        return { }
    },
    components: { }, 
    methods: { },
  }
</script>

