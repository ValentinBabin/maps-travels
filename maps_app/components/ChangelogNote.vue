<template>

  <section class="mb-5">
    <h2 class="text-gray-800 text-2xl font-semibold tracking-tight mb-1"><span class="text-lg">v{{ numVersion }}</span> {{ title }} <i class="text-base">({{ date }})</i></h2>
    <ul>
      <li v-for="item in description" :key="item"><p class="text-gray-800 text-lg font-normal leading-6 pl-3">{{ item }}</p></li>
    </ul>
  </section>

</template>

<script>
  export default {
    name: "ChangelogNote",
    props: ['numVersion', 'date', 'title' , 'description'],
    data: function () {
      return { }
    },
    components: { }, 
    methods: { }
  }
</script>
