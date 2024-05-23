<template>
	<div>
			<div class="container profile-container" v-if="!store.isProfile">
				<h1>Profile</h1>
				<p>유저 정보가 없습니다.ㅠㅠ </p>
				<button class="btn btn-primary" @click="editUser">유저 정보 만들기!</button>
			</div>
			<div v-else>
				<ProfileComponent />
			</div>
	</div>
</template>


<script setup>
import ProfileComponent from '@/components/ProfileComponent.vue'
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/counter'
const router = useRouter()
const store = useMovieStore()

const editUser = () => {
	router.push({ name: 'editprofile' })
}

onMounted(() => {
	store.getPerson()
})
</script>

<style>
.like_body {
  background-color: #f8f9fa;
  font-family: Arial, sans-serif;
}
.profile-container {
	text-align: center;
	margin-top: 100px;
	font-family: Arial, sans-serif;
}
.profile-container h1 {
		font-size: 2.5rem;
		font-weight: bold;
}
.profile-container p {
		font-size: 1.25rem;
		color: #6c757d;
}
.btn-primary {
		background-color: #4a67f5;
		border-color: #4a67f5;
		font-size: 1rem;
		padding: 10px 20px;
}
</style>