<template>
  <div class="card">
    <img :src="getImgPath(movie.poster_path)" alt="a" class="card-img-top">
    <div class="card-body">
      <h5 class="card-title">{{ movie.title }}</h5>
      <p class="card-text">{{ movie.overview }}</p>
  	</div>
  </div>
</template>

<script setup>
defineProps({
  movie: Object
})
const getImgPath = (path) => {
  return `https://image.tmdb.org/t/p/w500/${path}`
}
</script>

<style scoped>
</style>