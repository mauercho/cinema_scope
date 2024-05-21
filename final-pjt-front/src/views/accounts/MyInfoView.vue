<template>
	<div>
		<div class="container">
			<h1>회원정보</h1>
			<div class="container" v-if="!store.isProfile">
				<p>유저 정보가 없습니다. ㅠㅠ 만들어주세요</p>
				<button class="btn btn-outline-secondary" @click="editUser">유저 정보 입력</button>
				<!-- <RouterLink :to="{ name: 'editprofile' }" class="btn btn-primary">프로필 수정</RouterLink> -->
			</div>
			<div v-else>
				<ProfileComponent />
				<!-- <h2>username</h2>
				<p>유저 정보가 있습니다.</p>
				<img :src="store.personImage" alt="no image">
				<p>자기소개</p>
				<p>{{ store.personBio }}</p> -->
				<!-- 유저정보가 있으면 들어갈곳 isProfile는 true일거임. -->
			</div>
			<!-- <Router-view /> -->
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

<style scoped>

</style>