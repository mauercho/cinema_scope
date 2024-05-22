<template>
	<div class="container">
		<h2>오늘의 박스 오피스</h2>
	</div>
	<div class = 'container border'>

		<div v-for="movie in dailymovies">
			<DailyMovie :movie="movie" />
		</div>
		<!-- <form @submit.prevent="doaction">
			<button>userinfo 보자/</button>
		</form> -->
		<!-- <h1>홈</h1> -->
		<!-- <div v-for="movie in store.movies" :key="movie.id">
			<img :src="getImgPath(movie.poster_path)" alt="">
		</div> -->
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
import axios from 'axios'
import DailyMovie from '@/components/DailyMovieComponent.vue'

const KR_API_KEY = import.meta.env.VITE_KR_MOVIE_API_KEY
const router = useRouter()
const dailymovies = ref([])

// const doaction = function (){
// 	router.push({name: 'userdetail', params: {userId: 4}})
// }

onMounted(() => {
	nowFilmingMovie()
})

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
</script>

<style scoped>

</style>