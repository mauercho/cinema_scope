<template>
  <div class="container d-flex flex-column align-items-center">
    <img :src="getImgPath(movie.poster_path)" alt="" style="width: 20%">
    <h3>{{ movie.title }}</h3>
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
          <button type="submit" class="btn btn-primary">Favorite</button>
        </div>
        <div v-else>
          <button type="submit" class="btn btn-primary">Favorite 취소</button>
        </div>
      </div>
      <div v-else>
        <div v-if="!isFavor">
          <button type="submit" class="btn btn-primary">Favorite</button>
        </div>
        <div v-else>
          <button type="submit" class="btn btn-primary">Favorite 취소</button>
        </div>
      </div>
    </form>
    <p><span class="fw-bold">개봉일: </span>: {{ movie.release_date }}</p>
    <p><span class="fw-bold">러닝타임: </span> {{ movie.runtime }}분</p>
    <p><span class="fw-bold">TMDB 평점: </span> {{ movie.vote_average }}</p>
    <h3>장르</h3>
    <span v-for="genre in movie.genres">{{ genre.name }}</span>
    <h3>줄거리</h3>
    <p>{{ movie.overview }}</p>
    <form @submit.prevent="reviewCreate" class="card align-center row" :style="{width:'70%', marginBottom: '2rem'}">
      <label for="review">리뷰 작성하세용.</label>
      <textarea name="review" id="review" v-model="review"></textarea>
      <button>리뷰 작성</button>
    </form>

    <h3>리뷰 모음</h3>
    <UserReview />
    <!-- <button
      type="button"
      class="btn"
      @click="openModal"
      data-bs-toggle="modal"
      data-bs-target="#youtubeTrailerModal"
    >C% 유튜브 띄우기.
      <img src="http://wiki.hash.kr/images/9/97/%EC%9C%A0%ED%8A%9C%EB%B8%8C_%EB%A1%9EA%B3%A0.png" alt="Youtube" style="width: 36px">
    </button> -->
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

</style>
