<template>
	<div>
		<img v-if="store.personImage" :src="`${store.API_URL}${store.personImage}`" alt="no image">
		<h3>username</h3>
		<p>자기소개</p>
		<hr>
		<p>{{ store.personBio }}</p>
	</div>
	<h3>favorite movies</h3>
	<hr>
	<h3>좋아요 누른 영화</h3>
	<hr>
	<h3>내가 쓴 리뷰</h3>
</template>

<script setup>
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/counter'
const router = useRouter()
const store = useMovieStore()

onMounted(() => {
	store.getPersonProfile()
})

</script>

<style scoped>

</style>