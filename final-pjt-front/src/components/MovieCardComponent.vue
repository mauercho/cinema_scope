<template>
  <div class="movie">
    <img :src="getImgPath(movie.poster_path)" alt="a">
    <div class="movie-title">
      {{ movie.title }}
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