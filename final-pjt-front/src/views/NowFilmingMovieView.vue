<!-- daily 영화 받았음 -->
<template>
	<div class="container">
		<h2>현재 박스 오피스</h2>
	</div>
	<div v-for="movie in dailymovies" class="container">
		<DailyCard :movie="movie"/>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/counter'

const store = useMovieStore()
const dailymovies = ref([])
import axios from 'axios'
import DailyCard from '@/components/DailyCardComponent.vue'
const KR_API_KEY = import.meta.env.VITE_KR_MOVIE_API_KEY

onMounted(() =>  {
	nowFilmingMovie()
})
const nowFilmingMovie = function () {
	axios({
		method: 'get',
		url: `http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=${KR_API_KEY}&targetDt=${getYesterdayDate()}`
	})
	.then((response) => {
		dailymovies.value = response.data.boxOfficeResult.dailyBoxOfficeList
	})
	.catch((error) => {
		console.log(error)
	})
}
const getYesterdayDate = function() {
    const date = new Date()
    date.setDate(date.getDate() - 1)

    const year = date.getFullYear()
    const month = ('0' + (date.getMonth() + 1)).slice(-2)
    const day = ('0' + date.getDate()).slice(-2)

    return `${year}${month}${day}`
  }

</script>

<style scoped>

</style>