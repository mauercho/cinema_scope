<template>
	<div>
		<div class="container">
			<!-- {{ info }}  -->
			<h3>{{ username }}</h3>
			<p>팔로워 수: {{ followCount }} </p>
			<p>팔로잉 수: {{ followings_count }}</p>
			<!-- <button class="btn btn-outline-primary" @click="followUser">팔로우 버튼</button> -->
			<div v-if="isFollowed">
				<button class="btn btn-outline-primary" @click="followUser">언팔로우 버튼</button>
			</div>
			<div v-else>
				<button class="btn btn-outline-primary" @click="followUser">팔로우 버튼</button>
			</div>
			<h3>자기소개</h3>
			<p>{{ info.bio }}</p>
			<h3>favoirte movies</h3>
			<div class="row">
      <div v-for="movie in getRandomMovies(favorite_movies, 4)" :key="movie.id" class="col-3">
        <MovieCard
          :movie="movie"
          @click="goDetailPage(movie.tmdb_id, movie.id, movie.like_users, movie.favorite_users)"
        />
      </div>
			</div>
		<hr>
		<h3>좋아요 누른 영화</h3>
		<div class="row">
			<div v-for="movie in getRandomMovies(liked_movies, 4)" :key="movie.id" class="col-3">
				<MovieCard
					:movie="movie"
					@click="goDetailPage(movie.tmdb_id, movie.id, movie.like_users, movie.favorite_users)"
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
import { ref, onMounted, computed } from 'vue'
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
const followers = ref([])
const followings = ref([])
const followers_count = ref(null)
const followings_count = ref(null)

const isFollowed = computed(() => {
	return followers.value && followers.value.includes(store.userId)
})

const followCount = computed(() => {
	return followers_count.value
})

onMounted(() => {
	getOtherUser()
})

const goDetailPage = function(tmdbId, moviePk, likeUsers, favorites) {
  router.push(`/${tmdbId}`)
	store.movieId = moviePk
	store.likeUsers = likeUsers
	store.favorites = favorites
}

const getOtherUser = function () {
	axios({
		method: 'get',
		url: `${store.API_URL}/accounts/profile/${userId}/`,
	})
	.then((response) => {
		info.value = response.data
		favorite_movies.value = response.data.user.favorites
		liked_movies.value = response.data.user.like_movies
		reviews.value = response.data.user.review_set
		username.value = response.data.user.username
	})
	.then(() => {
		followers.value = info.value.user.followers
		followings.value = info.value.user.followings
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
const followUser = function() {
	axios({
		method: 'post',
		url: `${store.API_URL}/accounts/profile/${info.value.user.id}/follow/`,
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