<template>
  <section class="md:container md:mx-auto py-10">
    <h1 class="text-7xl font-bold tracking-tight text-gray-700">changelog</h1>
    <div class="my-5">
      <NuxtLink to="/" class="hover:underline">Retourner a la Map</NuxtLink>
    </div>
    <section>
      <ChangelogNote v-for="post in posts" :key="post.id" :numVersion="post.numVersion" :date="post.date" :title="post.title" :description="post.description"/>
    </section>
  </section>
</template>

<script lang="ts">

import Vue from 'vue';

// export default Vue.extend({});

export default {
  data: function () {
    return {
      posts: [
        {
          id:0, 
          numVersion:"1.0", 
          date:"mai 2021",
          title:"Integration Map",
          description:[
            "Integration simple de leaflet en HTML",
            "Injection des villes en PHP",
          ]
        },
        {
          id:1,
          numVersion:"2.0",
          date:"septembre 2021",
          title:"Passage sous Nuxt",
          description:[
            "Passage du mini projet sous Nuxt",
            "Intégration Leaflet / Vue",
            "Création WEB API pour récupérer les villes"
          ]
        },
        {
          id:2,
          numVersion:"2.1",
          date:"septembre 2021",
          title:"Ajout des photos",
          description:[
            "Ajout popup au clic sur la ville",
            "Ajout images par ville",
            "Ajout carousel par ville pour les photos"
          ]
        },
      ]
    }
  },
}

</script>
