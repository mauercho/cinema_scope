<template>
	<div class="border">
		<div class="card">
			<div class="card-header">
				{{movieRank}}위: {{ info.movieNm }}
			</div>
			<div class="card-body">
				<blockquote class="blockquote mt-3">
					<p>개봉일: {{ info.openDt }}</p>
					<p>상태: {{ info.prdtStatNm }}</p>
					<span>주연:  </span>
					<!-- 이 부분 splice 하는거 고쳐야함. -->
					<span v-for="actor in info.actors" class="actor-name">{{ actor.peopleNm }}</span>
					<br>
					<span>감독:  </span>
					<span v-for="director in info.directors">{{ director.peopleNm }}</span>
					<br>
					<span>등급:  </span>
					<span v-for="grade in info.audits">{{ grade.watchGradeNm }}</span>
					<br>
				</blockquote>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const KR_API_KEY = import.meta.env.VITE_KR_MOVIE_API_KEY
const info = ref([])

const props = defineProps({
	movie: Object,
})


const movieCd = ref(props.movie.movieCd)
const movieRank = ref(props.movie.rank)

onMounted(() => {
	getMovieDetail()
})

const getMovieDetail = function () {
	axios({
		method: 'get',
		url: `http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=${KR_API_KEY}&movieCd=${movieCd.value}`
	})
	.then((response) => {
		info.value = response.data.movieInfoResult.movieInfo
	})
	.catch((error) => {
		console.log(error)
	})
}

</script>

<style scoped>
.actor-name {
    margin-right: 10px;
}
</style>