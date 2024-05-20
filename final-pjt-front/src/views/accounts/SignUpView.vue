<template>
	<div>
		<div class="container">
			<h1>회원가입</h1>
			<form @submit.prevent="signup">
				<div>
					<label for="username">username : </label>
					<input type="text" v-model.trim="username" id="username">
				</div>
				<div>
					<label for="password1">password : </label>
					<input type="password" v-model.trim="password1" id="password1">
				</div>
				<div>
					<label for="password2">password 확인 : </label>
					<input type="password" v-model.trim="password2" id="password2">
					<input type="submit">
				</div>
			</form>
		</div>
	</div>
</template>

<script setup>
import { ref } from 'vue'
import { useMovieStore } from '@/stores/counter'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const store = useMovieStore()

const signup = function(){
	const payload = {
		username: username.value,
		password1: password1.value,
		password2: password2.value
	}
	store.signUp(payload)
}

</script>

<style scoped>

</style>