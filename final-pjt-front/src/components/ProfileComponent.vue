<template>
	<div class="container">
		<img v-if="store.personImage" :src="`${store.API_URL}${store.personImage}`" alt="no image">
		<br>
		<h3>{{ store.loginUserName }}</h3>
		<p>팔로워 수: {{ store.loginUserFollowers.length }}</p>
		<p>팔로잉 수: {{ store.loginUserFollowings.length }}</p>
		<button class="btn btn-outline-primary" @click="profileUpdate">유저 정보 수정</button>
		<p>자기소개</p>
		<p>{{ store.personBio }}</p>
		<hr>
	</div>
	<div class="container text-align-center">
	<h3>favorite movies</h3>
	<div class="row">
      <div v-for="movie in getRandomMovies(store.favoriteMovies, 4)" :key="movie.id" class="col-3">
				<MovieCard
          :movie="movie"
          @click="goDetailPage(movie.tmdb_id, movie.id, movie.like_users, movie.favorite_users)"
        />
      </div>
    </div>
	<hr>
	<h3>좋아요 누른 영화</h3>
	<div class="row">
		<!-- <div v-for="movie in store.likedMovies" :key="movie.id" class="col-3">
        <MovieCard
          :movie="movie"
          @click="goDetailPage(movie.tmdb_id)"
        />
      </div> -->
			<div v-for="movie in getRandomMovies(store.likedMovies, 4)" :key="movie.id" class="col-3">
				<MovieCard
					:movie="movie"
					@click="goDetailPage(movie.tmdb_id, movie.id, movie.like_users, movie.favorite_users)"
				/>
			</div>
		</div>
	<hr>
	<h3>내가 쓴 리뷰</h3>
	<div v-if="store.reviewsMovies.length > 0">
		<div v-for="review in store.reviewsMovies" :key="review.id">
			<MovieReview
				:review="review" class="mb-3 mt-3"
			/>
		</div>
	</div>
	<div v-else>
		<p>리뷰가 없습니다.</p>
	</div>
		<!-- <div v-for="review in store.reviewsMovies" :key="review.id">
			<MovieReview
				:review="review" class="mb-3 mt-3"
			/>
		</div> -->
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

<style scoped>

</style>