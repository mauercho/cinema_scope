<template>
  <div>
  <div class="movie-item">
    <img :src="getImgPath(movie.poster_path)" alt="a">
    <div class="movie-item-title">
      {{ movie.title }}
  	</div>
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
.movie-item {
		width: 200px;
		border-radius: 10px;
		overflow: hidden;
		text-align: center;
}
.movie-item img {
		width: 100%;
		height: 300px;
		object-fit: cover;
		border-bottom: 1px solid #ddd;
}
.movie-item-title {
		padding: 10px;
		font-size: 16px;
		font-weight: bold;
}
</style>