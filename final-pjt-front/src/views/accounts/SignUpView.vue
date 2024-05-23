<template>
	<div class="form-container">
		<h2 class="text-center">Sign up</h2>
		<form @submit.prevent="signup">
			<div class="mb-3">
				<label for="username" class="form-label">Username</label>
				<input type="text" class="form-control" v-model.trim="username" id="username" placeholder="Enter your username">
			</div>
			<div class="mb-3">
				<label for="password1" class="form-label">Password</label>
				<input type="password" class="form-control" v-model.trim="password1" id="password1" placeholder="Enter your password">
			</div>
			<div>
				<label for="password2" class="form-label">Password Confirmation</label>
				<input type="password" class="form-control" v-model.trim="password2" id="password2" placeholder="Re-enter your password">
			</div>
			<button type="submit" class="btn btn-primary">Sign Up</button>
			<div class="form-text">
				<p>Login if you already have an account!</p>
			</div>
		</form>
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
.form-container {
		max-width: 400px;
		margin: 50px auto;
		padding: 2rem;
		background-color: #ffffff;
		border-radius: 8px;
		box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.form-control {
		background-color: #f1f3f5;
		border: none;
		border-radius: 8px;
		padding: 1rem;
		margin-bottom: 1rem;
}
.btn-primary {
		background-color: #4a67f5;
		border: none;
		border-radius: 8px;
		padding: 1rem;
		width: 100%;
}
.btn-primary:hover {
		background-color: #3b55d1;
}
.form-text {
		text-align: center;
		margin-top: 1rem;
}
.form-text a {
		color: #6c757d;
		text-decoration: none;
}
.form-text a:hover {
		text-decoration: underline;
}
</style>