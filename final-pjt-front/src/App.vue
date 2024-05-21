
<template>
  <header>
    <div class ="container">
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <Router-link class="navbar-brand" :to="{ name: 'home' }"><img src="@/assets/logo.png" alt="Logo" id="logo"></Router-link>
        <div class="collapse navbar-collapse">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <Router-link class="nav-link" :to="{ name: 'home' }">현재상영중인 영화</Router-link>
            </li>
            <li class="nav-item">
              <Router-link class="nav-link" :to="{ name: 'recommended' }">영화 추천받기</Router-link>
            </li>
            <!-- <li class="nav-item">
              <Router-link class="nav-link" :to="{ name: 'myinfo', params: {userid: store.userId}}">내 프로필</Router-link>
            </li> -->
          </ul>
          <div v-if="store.token === null">
            <Router-link class="btn btn-outline-primary mr-5" :to="{ name: 'signup' }">회원가입</Router-link>
            <Router-link class="btn btn-outline-secondary" :to="{ name: 'login' }">로그인</Router-link>
          </div>
          <div v-else>
            <Router-link class="btn btn-outline-primary mr-5" :to="{ name: 'myinfo'}">내 정보</Router-link>
            <!-- <Router-link class="btn btn-outline-secondary" :to="{name: 'logout'}">로그아웃</Router-link> -->
            <button class="btn btn-outline-secondary" @click="handleLogout">로그아웃</button>
          </div>
          <!-- <form class="form-inline my-2 my-lg-0">
            <input class="form-control mr-sm-2" type="search" placeholder="영화 검색" aria-label="Search">
          </form> -->
        </div>
      </nav>
    </div>
  </header>
  <Router-view />
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useMovieStore } from '@/stores/counter'
import { useRouter } from 'vue-router'


const store = useMovieStore()
const router = useRouter()
const handleLogout = () => {
  store.logOut()
  router.push({ name: 'home' })
}


</script>

<style scoped>
#logo {
  width: 3rem; /* 원하는 너비로 설정 */
  height: auto; /* 높이는 자동으로 설정하여 비율을 유지 */
}
/* header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
} */
</style>
