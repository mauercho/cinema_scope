<template>
	<div>
		<div v-for="review in reverseReview" :key="review.id">
			<hr>
			<UserReview class="reviews"
				:review="review"
				@click="changePage(review.user.id)"
			/>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import UserReview from '@/components/UserReviewComponent.vue'
import axios from 'axios'
import { useMovieStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
const router = useRouter()

const store = useMovieStore()
onMounted(() => {
  getReview()
})

const reverseReview = ref(null)
const allReview = ref(null)

const changePage = function(otherUserId) {
	if (store.userId === otherUserId) {
		router.push({ name: 'myinfo' })
	} else {
		router.push({ name: 'userdetail', params: { userId: otherUserId } })
	}
}


const getReview = function () {
  axios({
    method: 'get',
    url: `${store.API_URL}/movies/${store.movieId}/reviews/`,
  })
  .then((response) => {
    allReview.value = response.data
    reverseReview.value = [...allReview.value].reverse()
  })
  .catch((error) => {
    console.log(error)
  })
}
</script>

<style scoped>
.reviews {
    margin-top: 20px;
}
</style>