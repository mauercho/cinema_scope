<template>
	<!-- <div class="container text-align-center">
		<h1>GPT 기반 추천</h1>
		<hr>
		<div class="row">
			<div v-for="movie in movies" :key="movie.tmdb_id" class="col-3">
				<MovieCard
					:movie="movie"
				/>
			</div>
		</div>
	</div> -->
	<div>
		<div class="container">
			<div class="movie-title">
				추천 영화
			</div>
			<div class="movie-subtitle">
				<!-- These are the movies recommended by GPT based on your preferences. -->
				당신의 선호도를 기반으로 GPT에서 추천한 영화입니다.
			</div>
				<div class="row">
				<div class="movie-grid col-3" v-for="movie in movies" :key="movie.tmdb_id">
				<MovieCard
					:movie="movie"
				/>
				</div>
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

.movie-title {
		font-size: 24px;
		font-weight: bold;
		margin-top: 20px;
}
.movie-subtitle {
		font-size: 16px;
		color: #666;
		margin-bottom: 20px;
}
.movie-grid {
		display: flex;
		flex-wrap: wrap;
		gap: 20px;
		justify-content: center;
}
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