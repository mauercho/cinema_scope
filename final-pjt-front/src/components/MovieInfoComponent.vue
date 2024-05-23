<template>
  <div class="container-fluid main-content">
    <div class="row">
      <div class="col-lg-6">
        <div class="position-relative">
          <img height="600" width="500" :src="getImgPath(movie.poster_path)" alt="">
    <!-- <h3>{{ movie.title }}</h3> -->
          <div class="position-absolute bottom-0 start-0 p-3">
            <h1 class="movie-title">{{ movie.title }}</h1>
          </div>
        </div>
        <div class="reviews">
          <h4>Reviews</h4>
        </div>
        <UserReview />
      <form @submit.prevent="reviewCreate" class="post-review">
        <input placeholder="리뷰 작성해주세요." type="text" v-model="review">
        <!-- <textarea name="review" id="review" v-model="review"></textarea> -->
        <button>POST Review</button>
      </form>
      </div>
      <div class="col-lg-4">
        <div class="actions">
        <form @submit.prevent="doLike">
          <div v-if="isLike===null">
            <div v-if="!isLiked">
            <button type="submit" class="btn btn-primary">좋아요</button>
            </div>
            <div v-else>
              <button type="submit" class="btn btn-primary">좋아요 취소</button>
            </div>
          </div>
          <div v-else>
            <div v-if="!isLike">
              <button type="submit" class="btn btn-primary">좋아요</button>
            </div>
            <div v-else>
              <button type="submit" class="btn btn-primary">좋아요 취소</button>
            </div>

          </div>
        </form>
        <form @submit.prevent="doFavorite">
          <div v-if="isFavor == null">
            <div v-if="!isFavorite">
              <button type="submit" class="do_button">Favorite</button>
            </div>
            <div v-else>
              <button type="submit" class="do_button">Favorite 취소</button>
            </div>
          </div>
          <div v-else>
            <div v-if="!isFavor">
              <button type="submit" class="do_button">Favorite</button>
            </div>
            <div v-else>
              <button type="submit" class="do_button">Favorite 취소</button>
            </div>
          </div>
        </form>
        </div>
        <div class="movie-details mt-3">
          <h5>Release Date</h5>
          <p>{{ movie.release_date }}</p>
          <h5>Runtime</h5>
          <p>{{ movie.runtime }}분</p>
          <h5>TMDB Rating</h5>
          <p>{{ movie.vote_average }}</p>
          <h5>Genre</h5>
          <span class="margin-bot" v-for="genre in movie.genres"> {{ genre.name }} </span>
          <h5>Synopsis</h5>
          <p>{{ movie.overview }}</p>
        </div>
      </div>
    <!-- <p><span class="fw-bold">개봉일: </span>: {{ movie.release_date }}</p>
    <p><span class="fw-bold">러닝타임: </span> {{ movie.runtime }}분</p>
    <p><span class="fw-bold">TMDB 평점: </span> {{ movie.vote_average }}</p>
    <h3>장르</h3>
    <span v-for="genre in movie.genres">{{ genre.name }}</span>
    <h3>줄거리</h3>
    <p>{{ movie.overview }}</p> -->
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'
import { useMovieStore } from '@/stores/counter'
import UserReview from '@/views/UserReviewView.vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const review = ref(null)
const reverseReview = ref(null)
const allReview = ref(null)
const tempArr = ref([])
const isLike = ref(null)
const isFavor = ref(null)
const store = useMovieStore()

const doLike = function() {
  axios({
    method: 'post',
    url: `${store.API_URL}/movies/${store.movieId}/likes/`,
    headers: {
      'Authorization': `Token ${store.token}`
    }
  })
  .then((response) => {
    console.log(response.data)
    isLike.value = response.data.is_liked
    console.log('좋아요 성공')
  })
  .catch((error) => {
    console.log(error)
  })
}

const doFavorite = function() {
  axios({
    method: 'post',
    url: `${store.API_URL}/movies/${store.movieId}/favorites/`,
    headers: {
      'Authorization': `Token ${store.token}`
    }
  })
  .then((response) => {
    console.log(response.data)
    isFavor.value = response.data.is_favorite
    console.log(store.favorites)
  })
  .catch((error) => {
    console.log(error)
  })
}

const props = defineProps({
  movie: Object,
})

const isFavorite = computed(() => {
  return store.favorites && store.favorites.includes(store.userId)
})


const isLiked = computed(() => {
  return store.likeUsers && store.likeUsers.includes(store.userId)
})


const getImgPath = (path) => {
  return `https://image.tmdb.org/t/p/w500/${path}`
}

const reviewCreate = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/movies/${store.movieId}/reviews/`,
    data : {
      content: review.value
    },
    headers: {
      'Authorization': `Token ${store.token}`
    }
  })
  .then((response) => {
    console.log("성공했습니다.")
    const currentRoute = router.currentRoute.value.fullPath
    router.replace('/').then(() => {
      router.replace(currentRoute)
    })
  })
  .catch((error) => {
    console.log(store.token.value)
    console.log(error)
  })
}


</script>

<style scoped>
.main-content {
    padding: 20px;
}
.movie-title {
    font-size: 2rem;
    font-weight: bold;
    color: #fff;
}
.movie-details {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.movie-details h4 {
    font-weight: bold;
}
.movie-details h5 {
    font-weight: bold;
}
.margin-bot {
  margin-bottom: 0.5rem;
}
.movie-details p {
    margin-bottom: 0.5rem;
}
.reviews {
    margin-top: 20px;
}
.review {
    display: flex;
    flex-direction: column;
    margin-bottom: 10px;
}
.review-content {
    background-color: #f1f1f1;
    padding: 10px;
    border-radius: 8px;
    width: 100%;
}
.review-content h6 {
    margin: 0;
    font-weight: bold;
}
.review-content p {
    margin: 0;
}
.post-review {
    display: flex;
    align-items: center;
    margin-top: 20px;
}
.post-review input {
    flex: 1;
    padding: 10px;
    border-radius: 20px;
    border: 1px solid #ccc;
    margin-right: 10px;
}
.post-review button {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 20px;
}
.sidebar {
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.sidebar h5 {
    font-weight: bold;
}
.sidebar .movie-item {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
}
.sidebar .movie-item img {
    border-radius: 8px;
    width: 60px;
    height: 60px;
    margin-right: 10px;
}
.sidebar .movie-item p {
    margin: 0;
}
.actions {
    display: flex;
    justify-content: flex-end;
    margin-top: 20px;
}
.do_button {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 20px;
    margin-left: 10px;
}
</style>
