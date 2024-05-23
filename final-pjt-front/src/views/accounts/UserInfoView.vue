<template>
	<div class="container">
		<div class="profile-header">
			<h2>{{ username }}</h2>
		<p>@minwu_97</p>
		</div>
		<div class="profile-stats">
				<div class="stat" v-if="first === null">
				<h3>{{ followers.length }} </h3>
				<p>Followers</p>
				</div>
				<div class="stat" v-else>
				<h3>{{ first.followers_count }}</h3>
				<p>Followers</p>
				</div>
				<div class="stat">
				<h3>{{ followings.length }}</h3>
				<p>Following</p>
				</div>
		</div>
			<!-- <button class="btn btn-outline-primary" @click="followUser">팔로우 버튼</button> -->
			<div v-if="first === null">
				<div class="follow-btn" v-if="isFollowed">
					<button @click="followUser">Unfollow</button>
				</div>
				<div class="follow-btn" v-else>
					<button @click="followUser">Follow</button>
				</div>
			</div>
			<div v-else>
				<div class="follow-btn" v-if="first.is_followed">
					<button @click="followUser">Unfollow</button>
				</div>
				<div class="follow-btn" v-else>
					<button @click="followUser">Follow</button>
				</div>
			</div>
			<div class="bio">
				<p>{{ info.bio }}</p>
			</div>
			<div class="section-title">
				Favorite Movies
			</div>
			<div class="row">
				<div class="movies col-3" v-for="movie in favorite_movies.slice(0, 4)" :key="movie.id">
					<MovieCard
						class="movies"
						:movie="movie"
						@click="goDetailPage(movie.tmdb_id, movie.id, movie.like_users, movie.favorite_users)"
					/>
				</div>
			</div>
		<hr>
		<div class="section-title">
			Liked Movies
		</div>
		<div class="row">
			<div class="movies col-3" v-for="movie in getRandomMovies(liked_movies, 8)" :key="movie.id">
				<MovieCard
					class="movies"
					:movie="movie"
					@click="goDetailPage(movie.tmdb_id, movie.id, movie.like_users, movie.favorite_users)"
				/>
			</div>
		</div>
		<div class="section-title">{{ username }}'s Reviews</div>
		<div class="user-reviews" v-for="review in reviews" :key="review.id">
			<MovieReview
				class="review"
				:review="review"
			/>
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
const first = ref(null)

const isFollowed = computed(() => {
	return followers.value && followers.value.includes(store.userId)
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
		first.value = response.data
		console.log(response)
	})
	.catch((error) => {
		console.log(error)
	})
}


</script>

<style scoped>
.profile-header {
		text-align: center;
		margin-top: 20px;
}
.profile-header h2 {
		margin-top: 10px;
		font-size: 24px;
}
.profile-header p {
		color: #6c757d;
}
.profile-stats {
		display: flex;
		justify-content: center;
		margin-top: 20px;
}
.profile-stats .stat {
		margin: 0 15px;
		text-align: center;
}
.profile-stats .stat h3 {
		font-size: 20px;
		margin-bottom: 5px;
}
.profile-stats .stat p {
		color: #6c757d;
}
.follow-btn {
		margin-top: 20px;
		text-align: center;
}
.follow-btn button {
		background-color: #007bff;
		color: white;
		border: none;
		padding: 10px 20px;
		border-radius: 5px;
}
.section-title {
		font-size: 25px;
		margin-top: 30px;
		margin-bottom: 10px;
}
.movies-section {
		display: flex;
		justify-content: center;
		flex-wrap: wrap;
}
.movies-section .movie {
		margin: 10px;
		border-radius: 10px;
		overflow: hidden;
		text-align: center;
}
.movies-section .movie img {
		width: 200px;
		height: 300px;
		object-fit: cover;
}
.movies-section .movie p {
		margin-top: 10px;
		font-size: 16px;
		color: #333;
}
.user-reviews {
		margin-top: 30px;
}
.user-reviews .review {
		margin-bottom: 20px;
		padding: 15px;
		background-color: #fff;
		border-radius: 10px;
		box-shadow: 0 4px 6px rgba(0, 0, 0, 0.4);
}
.user-reviews .review h5 {
		font-size: 16px;
		margin-bottom: 5px;
}
.user-reviews .review p {
		font-size: 14px;
		color: #333;
}
.bio {
		text-align: center;
		margin-top: 20px;
		font-size: 16px;
		color: #333;
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