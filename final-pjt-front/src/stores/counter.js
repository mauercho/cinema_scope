import { ref, computed, watch } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

const TMDB_API_KEY = import.meta.env.VITE_TMDB_API_KEY
const KR_API_KEY = import.meta.env.VITE_KR_MOVIE_API_KEY

export const useMovieStore = defineStore('counter', () => {
  const movies = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const userId = ref(null)
  const router = useRouter()
  const isProfile = ref(false)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const getPerson = function() {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/profile/${userId.value}/`,
    })
    .then((response) => {
      if (response.data.bio !== null) { // 프로필이 있을 떄
        isProfile.value = true
      }
      else {
        isProfile.value = false
      }
      // 프로필에 없을때는 false고 프로필을 만들어야함.
      // console.log(response.data)
      // console.log(response.data.bio)
    })
    .catch((error) => {
      console.log(error)
    })
  }

  const getMovies = function() {
    axios({
      method: 'get',
      url: `${API_URL}/movies/list/`,
    })
    .then((response) => {
      movies.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }
  const signUp = function(payload) {
    const { username, password1, password2 } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2
      }
    })
    .then((response) => {
      console.log('회원가입 성공!')
      const password = password1
      logIn({ username, password })
      // const password = password1
      // logIn({ username, password })
    })
    .catch((error) => {
      console.log(error)
    })
  }
  const logOut = function() {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
  })
    .then((response) => {
      console.log('로그아웃 성공!')
      token.value = null
    })
    .catch((error) => {
      console.log(error)
    })
  }


  const logIn = function (payload) {
    const { username, password } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
    .then((response) => {
      console.log('로그인 성공!')
      token.value = response.data.key

      // 로그인 성공 후 사용자 정보를 가져옵니다.
      return axios({
        method: 'get',
        url: `${API_URL}/accounts/user/`,
        headers: {
          'Authorization': `Token ${token.value}`
        }
      })
    })
    .then((response) => {
      console.log('사용자 정보:', response.data)
      // 여기서 response.data는 사용자 정보입니다.
      // 필요한 필드를 추출하여 사용하세요.
      userId.value = response.data.pk
      console.log('사용자 ID:', userId.value)
      router.push({ name : 'home' })
    })
    .catch((error) => {
      console.log(error)
    })
      // .then((response) => {
      //   // console.log('로그인 성공!')
      //   // console.log(response)
      //   // console.log(response.data.key)
      //   // 3. 로그인 성공 후 응답 받은 토큰을 저장
      //   console.log('로그인 성공!')
      //   console.log(response)
      //   token.value = response.data.key
      //   router.push({ name : 'home' })
      // })
      // .catch((error) => {
      //   console.log('실패')
      //   console.log(error)
      // })
  }

  return { movies, getMovies, signUp, logIn, token, isLogin, API_URL, userId, getPerson, logOut, isProfile}
}, {persist: true})

