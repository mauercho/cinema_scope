<template>
  <div>
    <MovieDetailInfo
      :movie="movie"
    />
  </div>
</template>

<script setup>

import MovieDetailInfo from '@/components/MovieInfoComponent.vue'
import {useRoute} from 'vue-router'
const API_KEY = import.meta.env.VITE_TMDB_API_KEY
import axios from 'axios'
// import {useCartStore} from '@/stores/counter'
import {ref, onMounted} from 'vue'
const route = useRoute()
const movie = ref([])
const movieId = route.params.movieId
const likeUsers = ref([])
const getMovie = function(movieId) {
    axios({
      method: 'get',
      url: `https://api.themoviedb.org/3/movie/${movieId}?api_key=${API_KEY}&language=ko-KR`
    })
    .then((response) => {
      movie.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }
  onMounted(() => {
    getMovie(movieId)
  })
</script>

<style scoped>

</style>