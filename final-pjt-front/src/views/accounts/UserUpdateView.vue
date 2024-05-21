<template>
	<div class="container" v-if="store.personImage">
		<!-- 이미지가 있고 수정만 하면 되는 거임. -->
		<h1>유저 정보 수정 페이지입니다.</h1>
		<form @submit.prevent="editProfile">
			<label for="self-introduction">자기소개: </label>
			<textarea name="self-introduction" id="self-introduction" v-model="selfIntroduction" required></textarea>
			<br>
			<label for="image-input">이미지 넣으세요.</label>
			<br>
			<input label="image-input" type = "file" accept = "image/*" @change="previewImage">
			<img :src="imagePreview2" alt="Image preview" v-if="imagePreview2"/>
			<br>
			<button type="submit">수정하기</button>
		</form>
	</div>
	<div class="container" v-else>
		<h1>유저 정보 생성 페이지입니다.</h1>
		<form @submit.prevent="createProfile">
			<label for="self-introduction">자기소개: </label>
			<textarea name="self-introduction" id="self-introduction" v-model="selfIntroduction" required></textarea>
			<br>
			<label for="image-input">이미지 넣으세요.</label>
			<br>
			<input label="image-input" type = "file" accept = "image/*" @change="previewImage">
			<img :src="imagePreview2" alt="Image preview" v-if="imagePreview2"/>
			<br>
			<button type="submit">수정하기</button>
		</form>
	</div>
</template>

<script setup>
import { ref } from 'vue'
import { useMovieStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
import axios from 'axios'

const store = useMovieStore()
const router = useRouter()
const imagePreview = ref(null)
const selfIntroduction = ref(null)
const imagePreview2 = ref(null)

const editProfile = function () {
		const formData = new FormData()
    formData.append('bio', selfIntroduction.value)
    formData.append('profile_pic', imagePreview.value)
    axios({
        method: 'put',
        url: `${store.API_URL}/accounts/profile/${store.userId}/`,
        data: formData,
    })
    .then((response) => {
        console.log("프로필 수정 완료")
        console.log(response)
        router.push({ name: 'home' })
    })
    .catch((error) => {
        console.log(error)
    })

}

const createProfile = function () {
    const formData = new FormData()
    formData.append('bio', selfIntroduction.value)
    formData.append('profile_pic', imagePreview.value)

    axios({
        method: 'post',
        url: `${store.API_URL}/accounts/profile/${store.userId}/`,
        data: formData,
    })
    .then((response) => {
        console.log("프로필 생성 완료")
        console.log(response)
        router.push({ name: 'home' })
    })
    .catch((error) => {
        console.log(error)
    })
}

function previewImage(event) {
    const file = event.target.files[0]
		const reader = new FileReader()
		reader.onload = (e) => {
			imagePreview2.value = e.target.result
		}
		reader.readAsDataURL(file)
    imagePreview.value = file
}

// function previewImage(event) {
//     const file = event.target.files[0]
//     imagePreview.value = file
// }

// function previewImage(event) {
//   const file = event.target.files[0]
//   const reader = new FileReader()
//   reader.onload = (e) => {
//     imagePreview.value = e.target.result
//   }
//   reader.readAsDataURL(file)
// }

</script>

<style scoped>

</style>