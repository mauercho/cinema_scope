import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import RecommendedView from '@/views/RecommendedView.vue'
import NowFilmingMovieView from '@/views/NowFilmingMovieView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import SignUpView from '@/views/accounts/SignUpView.vue'
import UserInfoView from '@/views/accounts/UserInfoView.vue'
import UserUpdateView from '@/views/accounts/UserUpdateView.vue'
import MyInfoView from '@/views/accounts/MyInfoView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/recommended',
      name: 'recommended',
      component: RecommendedView
    },
    {
      path: '/now-filming-movie',
      name: 'now-filming-movie',
      component: NowFilmingMovieView
    },
    {
      path: '/:movieId',
      name: 'detail',
      component: MovieDetailView
    },
    {
      path: '/accounts/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/accounts/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/accounts/userinfo',
      name: 'userinfo',
      component: UserInfoView
    },
    {
      path: '/accounts/userupdate',
      name: 'userupdate',
      component: UserUpdateView
    },
    {
      path: '/accounts/myinfo/',
      name: 'myinfo',
      component: MyInfoView
    },
  ]
})

import { useMovieStore } from '@/stores/counter'
router.beforeEach((to, from) => {
  const store = useMovieStore()
  // 인증되지 않은 사용자는 메인 페이지에 접근 할 수 없음
  if (to.name === 'myinfo' && store.isLogin === false) {
    window.alert('로그인이 필요해요!!')
    return { name: 'login' }
  }

  // 인증된 사용자는 회원가입과 로그인 페이지에 접근 할 수 없음
  if ((to.name === 'signup' || to.name === 'login') && (store.isLogin === true)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'home' }
  }
})


export default router
