<template>
	<div>
    <div class="form-container">
      <h2 class="text-center">Login</h2>
      <form @submit.prevent="logIn">
        <div class="mb-3">
          <label for="username" class="form-label">Username</label>
          <input type="text" class="form-control" v-model.trim="username" id="username" placeholder="Enter your username">
        </div>
        <div class="mb-3">
          <label for="password" class="form-label">Password</label>
          <input type="password" class="form-control" v-model.trim="password" id="password" placeholder="Enter your password">
        </div>
        <button type="submit" class="btn btn-primary">Login</button>
      </form>
      <div class="text-center mt-3">
        <p>Don't have an account?</p>
        <a href="#">Sign up</a>
      </div>
    </div>
	</div>
</template>

<script setup>
import { ref } from 'vue'
import { useMovieStore } from '@/stores/counter'

const username = ref(null)
const password = ref(null)
const store = useMovieStore()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}

</script>

<style scoped>
.like_body {
  background-color: #f8f9fa;
  font-family: Arial, sans-serif;
}
.form-container {
    max-width: 400px;
    margin: 100px auto;
    padding: 20px;
    background-color: #ffffff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
.form-control {
    background-color: #f1f3f5;
    border: none;
    border-radius: 8px;
    padding: 10px;
}
.btn-primary {
    background-color: #4a6cf7;
    border: none;
    border-radius: 8px;
    padding: 10px;
    width: 100%;
}
.btn-primary:hover {
    background-color: #3b5bdb;
}
.text-center a {
    color: #6c757d;
    text-decoration: none;
}
.text-center a:hover {
    text-decoration: underline;
}
</style>