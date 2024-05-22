<template>
	<div>
		<div class="container">
			{{ info }}
			<h3>{{ username }}</h3>
			<button class="btn btn-outline-primary" @click="followUser">팔로우 버튼</button>
			<!-- <div v-if="is_followed === false">
				<button class="btn btn-outline-primary" @click="followUser">팔로우 버튼</button>
			</div>
			<div v-else>
				<button class="btn btn-outline-primary" @click="followUser">언팔로우 버튼</button>
			</div> -->
			<h3>자기소개</h3>
			<p>{{ info.bio }}</p>
			<h3>favoirte movies</h3>
			<div class="row">
      <div v-for="movie in getRandomMovies(favorite_movies, 4)" :key="movie.id" class="col-3">
        <MovieCard
          :movie="movie"
          @click="goDetailPage(movie.tmdb_id, movie.id)"
        />
      </div>
			</div>
		<hr>
		<h3>좋아요 누른 영화</h3>
		<div class="row">
			<div v-for="movie in getRandomMovies(liked_movies, 4)" :key="movie.id" class="col-3">
				<MovieCard
					:movie="movie"
					@click="goDetailPage(movie.tmdb_id, movie.id)"
				/>
			</div>
		</div>
		<h3> {{ username }}님이 쓴 리뷰</h3>
		<div v-if="reviews.length > 0">
			<div v-for="review in reviews" :key="review.id">
			<MovieReview
				:review="review" class="mb-3 mt-3"
			/>
			</div>
		</div>
		<div v-else>
			<p>리뷰가 없습니다.</p>
		</div>

		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/counter'
import axios from 'axios'
import MovieCard from '@/components/MovieCardComponent.vue'
import { useRoute, useRouter } from 'vue-router'
import MovieReview from '@/components/MovieReviewComponent.vue'

const username = ref(null)
const route = useRoute()
const store = useMovieStore()
const userId = route.params.userId
const info = ref([])
const favorite_movies = ref([])
const liked_movies = ref([])
const reviews = ref([])
const router = useRouter()
const is_followed = ref(false)

onMounted(() => {
	getOtherUser()
})

const goDetailPage = function(tmdbId, moviePk) {
  router.push(`/${tmdbId}`)
	store.movieId = moviePk
}

const getOtherUser = function () {
	axios({
		method: 'get',
		url: `${store.API_URL}/accounts/profile/${userId}/`,
	})
	.then((response) => {
		// console.log(response.data)
		info.value = response.data
		favorite_movies.value = response.data.user.favorites
		liked_movies.value = response.data.user.like_movies
		reviews.value = response.data.user.review_set
		username.value = response.data.user.username
	})
	// .then(() => {
	// 	axios({
	// 		method: 'post',
	// 		url: `${store.API_URL}/accounts/profile/${info.value.id}/follow/`,
	// 		headers: {
	// 			'Authorization': `Token ${store.token}`
	// 		}
	// 	})
	// 	.then((response) => {
	// 		// console.log('팔로우 1성공')
	// 		// console.log(response)
	// 		is_followed.value = !response.data.is_followed
	// 		console.log(is_followed.value)
	// 	})
	// 	.catch((error) => {
	// 		console.log(error)
	// 	})
	// })
	// .then(() => {
	// 	axios({
	// 		method: 'post',
	// 		url: `${store.API_URL}/accounts/profile/${info.value.id}/follow/`,
	// 		headers: {
	// 			'Authorization': `Token ${store.token}`
	// 		}
	// 	})
	// 	.then((response) => {
	// 		console.log('팔로우 2성공')
	// 		console.log(response)
	// 	})
	// })
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
const followUser = function() {
	axios({
		method: 'post',
		url: `${store.API_URL}/accounts/profile/${info.value.id}/follow/`,
		headers: {
      'Authorization': `Token ${store.token}`
    }
	})
	.then((response) => {
		console.log(response)
	})
	.catch((error) => {
		console.log(error)
	})
}


</script>

<style scoped>

</style>