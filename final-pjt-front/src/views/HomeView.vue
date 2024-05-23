<template>
	<div class="like_body">
		<div class="content">
			<div class="movie-rankings">
				<h2>Today's Movie Rankings</h2>
			</div>
			<div v-for="movie in dailymovies">
				<DailyMovie :movie="movie" />
			</div>
		</div>
	</div>
	<br>
	<br>
	<div class="container">
		<div class="section-title">
			랜덤 추천 영화
		</div>
		<div class="row">
			<div class="movies col-3" v-for="movie in getRandomMovies(store.movies, 8)" :key="movie.id">
					<MovieCard
						class="movies"
						:movie="movie"
						@click="goDetailPage(movie.tmdb_id)"
					/>
					</div>
		</div>	
		<!-- {{ store.movies }} -->
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
import axios from 'axios'
import DailyMovie from '@/components/DailyMovieComponent.vue'
import MovieCard from '@/components/MovieCardComponent.vue'

const KR_API_KEY = import.meta.env.VITE_KR_MOVIE_API_KEY
const router = useRouter()
const dailymovies = ref([])
const store = useMovieStore()

// const doaction = function (){
// 	router.push({name: 'userdetail', params: {userId: 4}})
// }

onMounted(() => {
	nowFilmingMovie()
	store.getMovies()
})

const goDetailPage = function(tmdbId)
{
	router.push(`/${tmdbId}`)
}

const getYesterdayDate = function() {
    const date = new Date()
    date.setDate(date.getDate() - 1)

    const year = date.getFullYear()
    const month = ('0' + (date.getMonth() + 1)).slice(-2)
    const day = ('0' + date.getDate()).slice(-2)

    return `${year}${month}${day}`
  }

const nowFilmingMovie = function () {
	axios({
		method: 'get',
		url: `http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=${KR_API_KEY}&targetDt=${getYesterdayDate()}`
	})
	.then((response) => {
		dailymovies.value = response.data.boxOfficeResult.dailyBoxOfficeList
		console.log(dailymovies.value)
	})
	.catch((error) => {
		console.log(error)
	})
}

function getRandomMovies(movies, count) {
    // Copy the array to avoid modifying the original
    const copiedMovies = [...movies]

    // Shuffle the array
    for (let i = copiedMovies.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1))
      const temp = copiedMovies[i]
      copiedMovies[i] = copiedMovies[j]
      copiedMovies[j] = temp
    }

    // Return the first `count` elements
    return copiedMovies.slice(0, count)
  }

</script>

<style scoped>
.like_body {
	font-family: Arial, sans-serif;
	text-align: center;
	background-color: white;
}

.navbar-brand {
		font-weight: bold;
}
.content {
		margin: 20px;
}
.movie-rankings {
		margin-top: 20px;
}
.movie-rankings h2 {
		font-weight: bold;
}
.movie-rankings ul {
		list-style: none;
		padding: 0;
		display: inline-block;
		text-align: left;
}
.movie-rankings li {
		display: flex;
		align-items: center;
		margin-bottom: 10px;
}
.movie-rankings li input {
		margin-right: 10px;
}
.recommended-movies {
		margin-top: 40px;
}
.recommended-movies h2 {
		font-weight: bold;
}
.recommended-movies .movie-card {
		display: inline-block;
		margin: 10px;
		text-align: center;
		border: 1px solid #ddd;
		border-radius: 10px;
		padding: 10px;
		/* background-color: #fff; */
}
.recommended-movies img {
		width: 150px;
		height: 200px;
		border-radius: 10px;
}

.section-title {
		font-size: 25px;
		margin: 30px 0 10px;
}

.movies {
		display: flex;
		justify-content: center;
		flex-wrap: wrap;
}
.movies .movie {
		width: 200px;
		margin: 10px;
		border-radius: 10px;
		overflow: hidden;
		background-color: #fff;
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
		text-align: center;
}
.movies .movie img {
		width: 100%;
		height: 300px;
		object-fit: cover;
}
.movies .movie-title {
		padding: 10px;
		font-size: 16px;
		color: #333;
}

</style>