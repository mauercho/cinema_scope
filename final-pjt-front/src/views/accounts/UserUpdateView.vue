<template>
	<div class="container">
		<h1>유저 정보 수정 페이지입니다.</h1>
		<form @submit.prevent="createProfile">
			<label for="self-introduction">자기소개: </label>
			<!-- <input type="text" id="self-introduction" v-model="selfIntroduction" required> -->
			<textarea name="self-introduction" id="self-introduction" v-model="selfIntroduction" required></textarea>
			<br>
			<label for="image-input">이미지 넣으세요.</label>
			<input label="image-input" type = "file" accept = "image/*" @change="previewImage">
			<img :src="imagePreview" alt="Image preview" v-if="imagePreview"/>
			<button type="submit">수정하기</button>
		</form>
	</div>
</template>

<script setup>
import { ref } from 'vue'
import { useMovieStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useMovieStore()
const router = useRouter()
const imagePreview = ref(null)
const createProfile = function () {

}

function previewImage(event) {
    const file = event.target.files[0]
    const reader = new FileReader()
    reader.onload = (e) => {
        imagePreview.value = e.target.result
    }
    reader.readAsDataURL(file)
}


</script>

<style scoped>

</style>