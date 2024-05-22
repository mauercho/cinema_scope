<template>
  {{ movie }}
  <div class="container d-flex flex-column align-items-center">
    <img :src="getImgPath(movie.poster_path)" alt="" style="width: 20%">
    <h3>{{ movie.title }}</h3>
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

const review = ref(null)
const reverseReview = ref(null)
const allReview = ref(null)
const store = useMovieStore()
defineProps({
  movie: Object
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
  })
  .catch((error) => {
    console.log(store.token.value)
    console.log(error)
  })
}


</script>

<style scoped>

</style>
