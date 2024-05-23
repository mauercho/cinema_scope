<template>
	<div class="container text-align-center">
		<h1>GPT 기반 추천</h1>
		<hr>
		<div class="row">
			<div v-for="movie in movies" :key="movie.tmdb_id" class="col-3">
				<MovieCard
					:movie="movie"
				/>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/counter'
import MovieCard from '@/components/GptCardComponent.vue'
import axios from 'axios'

const store = useMovieStore()
const movies = ref([])


onMounted(() => {
	getGptMovies()
})

const getGptMovies = function() {
	axios({
		method: 'get',
		url: `${store.API_URL}/movies/recommend/${store.userId}/`,
	})
	.then((response) => {
		movies.value = response.data.recommendations
	})
	.catch((error) => {
		console.log(error)
	})
}
</script>

<style scoped>

</style>