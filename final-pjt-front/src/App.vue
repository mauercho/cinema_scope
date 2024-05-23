
<template>
  <header>
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <Router-link class="navbar-brand" :to="{ name: 'home' }"><img src="@/assets/logo.png" alt="Logo" id="logo">CINEMA SCOPE</Router-link>
          <div class="collapse navbar-collapse">
            <ul class="navbar-nav me-auto mb-lg-0">
              <li class="nav-item">
                <Router-link class="nav-link" :to="{ name: 'now-filming-movie' }">BOX OFFICE</Router-link>
              </li>
              <li class="nav-item">
                <Router-link class="nav-link" :to="{ name: 'recommended' }">RECOMMENDATION</Router-link>
              </li>
              <li class="nav-item">
                <Router-link class="nav-link" :to="{ name: 'myinfo'}">My Profile</Router-link>
              </li>
              <li class="nav-item">
                <Router-link class="nav-link" :to="{ name: 'signup' }">Sign-In</Router-link>
              </li>
            </ul>
            <div v-if="store.token === null" class="d-flex">
              <Router-link class="btn btn-primary" :to="{ name: 'login' }">Login</Router-link>
            </div>
            <div v-else class="d-flex">
              <button class="btn btn-primary" @click="handleLogout">Logout</button>
            </div>
        </div>
      </div>
      </nav>
  </header>
  <Router-view />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useMovieStore } from '@/stores/counter'
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'

const store = useMovieStore()
const router = useRouter()
const handleLogout = () => {
  store.logOut()
  router.push({ name: 'home' })
}
</script>

<style scoped>
#logo {
  width: 50px; /* 원하는 너비로 설정 */
  height: auto; /* 높이는 자동으로 설정하여 비율을 유지 */
}
.navbar-brand {
    font-weight: bold;
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
