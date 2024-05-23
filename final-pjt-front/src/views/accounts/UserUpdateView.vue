<template>
	<div class="container" v-if="store.personImage">
		<!-- 이미지가 있고 수정만 하면 되는 거임. -->
		<h2 class="mb-4">Edit Profile</h2>
		<form class="mb-3" @submit.prevent="editProfile">
			<label class="form-label" for="self-introduction">Bio</label>
			<textarea class="form-control" name="self-introduction" id="self-introduction" v-model="store.personBio" rows="3" required></textarea>
			<br>
			<input class="btn btn-attach me-2" label="image-input" type = "file" accept = "image/*" @change="previewImage">
			<img class="image-preview" height="400" :src="imagePreview2" alt="Image preview" v-if="imagePreview2"/>
			<br>
			<button type="submit" class="btn-save btn">Save</button>
		</form>
	</div>
	<div class="container" v-else>
		<h2 class="mb-4">Create Profile</h2>
		<form @submit.prevent="createProfile">
			<label class="form-label" for="self-introduction">Bio</label>
			<textarea class="form-control" name="self-introduction" id="self-introduction" v-model="selfIntroduction" required></textarea>
			<br>
			<input class="btn btn-attach me-2" label="image-input" type = "file" accept = "image/*" @change="previewImage">
			<img class="image-preview" height="400" :src="imagePreview2" alt="Image preview" v-if="imagePreview2"/>
			<br>
			<button type="submit" class="btn-save btn">Save</button>
		</form>
	</div>
</template>

<script setup>
import { ref } from 'vue';
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
		formData.append('bio', store.personBio)
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

function previewImage(event) {
    const file = event.target.files[0]
		const reader = new FileReader()
		reader.onload = (e) => {
			imagePreview2.value = e.target.result
		}
		reader.readAsDataURL(file)
    imagePreview.value = file
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

</script>

<style scoped>
.profile-pic {
		width: 40px;
		height: 40px;
		border-radius: 50%;
}
.container {
		max-width: 600px;
		margin-top: 50px;
}
.form-label {
		font-weight: bold;
}
.form-control {
		background-color: #f1f3f5;
		border: none;
		border-radius: 10px;
}
.btn-attach {
		background-color: #e0e0e0;
		color: black;
}
.btn-save {
		background-color: #4a90e2;
		color: white;
}
.image-preview {
		width: 100%;
		border-radius: 10px;
		margin-top: 20px;
}
</style>