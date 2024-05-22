<template>
	<div>
		<div v-if="reverseReview">
			<div v-for="review in reverseReview" :key="review.id">
				{{ review }}
				<hr>
				<UserReview
					:review="review" class="mb-3 mt-3"
					@click="changePage(review.user.id)"
				/>
			</div>
		</div>
		<div v-else>
			<p>리뷰가 없습니다.</p>
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

</style>