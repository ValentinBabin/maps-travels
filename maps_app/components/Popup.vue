<template>

    <section class="px-2 bg-gray-100 h-full">
        <p class="w-full text-center pt-2">{{ name }}, {{ date }}</p>
    </section>

</template>

<script>
  export default {
    name: "Popup",
    props: ["id", "name", "date"],
    data: function () {
        return { }
    },
    components: { }, 
    methods: { },
  }
</script>

<style type="scss" scoped>
    .map {
        height: 100vh;
    }
</style>
