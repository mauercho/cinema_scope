<template>
	<div class="container font-style">
		<div class="profile-header">
			<img height="150" width="150" v-if="store.personImage" :src="`${store.API_URL}${store.personImage}`" alt="no image">
		<h1>{{ store.loginUserName }}</h1>
		<p>minwu_97</p>
		<button class="btn-edit-profile" @click="profileUpdate">Edit Profile</button>
		</div>
		<div class="stats">
			<div class="stat">
				<h3>{{ store.loginUserFollowers.length }}</h3>
				<p>Followers</p>
			</div>
			<div class="stat">
				<h3>{{ store.loginUserFollowings.length }}</h3>
				<p>Followings</p>
			</div>
		</div>
		<div class="bio">
			<p>{{ store.personBio }}</p>
		</div>
	<div class="section-title">
		Favorite 영화
	</div>
	<div class="row">
      <div class="movies col-3" v-for="movie in store.favoriteMovies.slice(0, 4)" :key="movie.id">
				<MovieCard
          :movie="movie"
          @click="goDetailPage(movie.tmdb_id, movie.id, movie.like_users, movie.favorite_users)"
        />
      </div>
    </div>
	<hr>
	<div class="section-title">
		좋아하는 영화
	</div>
	<div class="row">
			<div class="movies col-3" v-for="movie in getRandomMovies(store.likedMovies, 8)" :key="movie.id">
				<MovieCard
					class="movies"
					:movie="movie"
					@click="goDetailPage(movie.tmdb_id, movie.id, movie.like_users, movie.favorite_users)"
				/>
			</div>
		</div>
	<hr>
	<div class="section-title">
		내가 쓴 리뷰
	</div>
	<div class="user-reviews" v-for="review in store.reviewsMovies" :key="review.id">
		<MovieReview
			class="review"
			:review="review"
		/>
	</div>
	</div>
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/counter'
import MovieCard from '@/components/MovieCardComponent.vue'
import MovieReview from '@/components/MovieReviewComponent.vue'
const router = useRouter()
const store = useMovieStore()


onMounted(() => {
	store.getPersonProfile()
	store.getAllInfoMovies()
})

function profileUpdate() {
	router.push({ name: 'editprofile' })
}

const goDetailPage = function(tmdbId, moviePk, likeUsers, favorites) {
  router.push(`/${tmdbId}`)
	store.movieId = moviePk
	store.likeUsers = likeUsers
	store.favorites = favorites
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

<style>
.profile-header {
		text-align: center;
		margin-top: 20px;
}
.profile-header img {
		width: 150px;
		height: 150px;
		border-radius: 50%;
}
.profile-header h1 {
		font-size: 24px;
		margin-top: 10px;
}
.profile-header p {
		color: #6c757d;
}
.stats {
		display: flex;
		justify-content: center;
		margin-top: 20px;
}
.stats .stat {
		margin: 0 15px;
		text-align: center;
}
.stats .stat h3 {
		font-size: 20px;
		margin-bottom: 5px;
}
.stats .stat p {
		color: #6c757d;
}
.btn-edit-profile {
		display: block;
		margin: 20px auto;
		padding: 10px 20px;
		background-color: #e0e0e0;
		border: none;
		border-radius: 5px;
		color: #000;
		font-size: 14px;
}
.bio {
		text-align: center;
		margin-top: 20px;
		font-size: 16px;
		color: #333;
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

.font-style {
	font-family: Arial, sans-serif;
}
</style>