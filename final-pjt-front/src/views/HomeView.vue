<template>
	<div class = 'container'>
		<h1>홈화면입니다.</h1>
		<!-- <h1>홈</h1> -->
		<!-- <div v-for="movie in store.movies" :key="movie.id">
			<img :src="getImgPath(movie.poster_path)" alt="">
		</div> -->
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/counter'


</script>

<style scoped>

</style>