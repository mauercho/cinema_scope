<template>
	<div class = 'container'>
		<h1>홈</h1>
		<div v-for="movie in store.movies" :key="movie.id">
			<img :src="getImgPath(movie.poster_path)" alt="">
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/counter'

const store = useMovieStore()

onMounted(() => {
	store.getMovies()
})
const getImgPath = (path) => {
  return `https://image.tmdb.org/t/p/w500/${path}`
}
</script>

<style scoped>

</style>