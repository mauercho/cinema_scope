
<template>
	<div>
		<div class="container">
		<h1 class="mt-5">Currently Showing Movies</h1>
		<h5 class="mt-4">Today's BoxOffice</h5>
		<div class="table-responsive">
		<table class="table table-bordered mt-3">
				<thead>
					<tr>
						<th>Movie Name</th>
						<th>Director</th>
						<th>GradeNm</th>
						<th>Actors</th>
					</tr>
				</thead>
				<tbody>
					<DailyCardComponent v-for="movie in dailymovies" :key="movie.movieCd" :movie="movie" />
				</tbody>
			</table>
		</div>

		<h5 class="mt-4">Get Tickets</h5>
			<div class="btn-group mt-3" role="group" aria-label="Get Tickets">
				<button @click.prevent="goMega" type="button" class="btn btn-primary">Mega Box</button>
				<button @click.prevent="goCGV" type="button" class="btn btn-danger">CGV</button>
				<button @click.prevent="goLotte" type="button" class="btn btn-warning">Lotte Cinema</button>
			</div>
		</div>
	</div>
</template>

<script setup>

import { ref, onMounted } from 'vue'
import axios from 'axios'
import DailyCardComponent from '@/components/DailyCardComponent.vue'
import { useMovieStore } from '@/stores/counter'
const store = useMovieStore()
const dailymovies = ref([])
const KR_API_KEY = import.meta.env.VITE_KR_MOVIE_API_KEY
onMounted(() => {
  nowFilmingMovie()
})
const nowFilmingMovie = () => {
axios({
	method: 'get',
	url: `http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=${KR_API_KEY}&targetDt=${getYesterdayDate()}`
})
.then((response) => {
	const movieList = response.data.boxOfficeResult.dailyBoxOfficeList
	const movieDetailsPromises = movieList.map(movie => getMovieDetails(movie.movieCd))
	Promise.all(movieDetailsPromises)
		.then(detailsList => {
			dailymovies.value = movieList.map((movie, index) => ({
				...movie,
				director: detailsList[index].directors.join(", "),
				gradeNm: detailsList[index].gradeNm,
				actors: detailsList[index].actors.join(", ")
			}))
		})
})
.catch((error) => {
	console.error(error)
})
}

const getMovieDetails = (movieCd) => {
return new Promise((resolve, reject) => {
	axios({
		method: 'get',
		url: `http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=${KR_API_KEY}&movieCd=${movieCd}`
	})
	.then((response) => {
		const movieInfo = response.data.movieInfoResult.movieInfo
		resolve({
			directors: movieInfo.directors.map(director => director.peopleNm),
			gradeNm: movieInfo.audits.map(audit => audit.watchGradeNm).join(", "),
			actors: movieInfo.actors.slice(0, 3).map(actor => actor.peopleNm) // 배우 정보는 3명까지 가져옴
		})
	})
	.catch((error) => {
		reject(error)
	})
})
}

const getYesterdayDate = () => {
const date = new Date()
date.setDate(date.getDate() - 1)
const year = date.getFullYear()
const month = ('0' + (date.getMonth() + 1)).slice(-2)
const day = ('0' + date.getDate()).slice(-2)
return `${year}${month}${day}`
}

function goMega() {
  window.open("http://www.megabox.co.kr/booking", "_blank", "width=500, height=500");
}
function goCGV() {
  window.open("http://www.cgv.co.kr/ticket/", "_blank", "width=500, height=500");
}
function goLotte() {
	window.open("http://www.lottecinema.co.kr/NLCHS/Ticketing", "_blank", "width=500, height=500");
}
	</script>



<style scoped>

body {
font-family: 'Arial', sans-serif;
background-color: #f8f9fa;
color: #212529;
}

.container {
margin-top: 50px;
}

.table th, .table td {
vertical-align: middle;
}

.btn-group .btn {
margin-right: 10px;
}

</style>