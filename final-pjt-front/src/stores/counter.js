import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

const TMDB_API_KEY = import.meta.env.VITE_TMDB_API_KEY
const KR_API_KEY = import.meta.env.VITE_KR_MOVIE_API_KEY

export const useMovieStore = defineStore('counter', () => {
  const movies = ref([])
  const API_URL = 'http://127.0.0.1:8000'
  const getMovies = function() {
    axios({
      method: 'get',
      // url: `https://api.themoviedb.org/3/movie/top_rated?api_key=${API_KEY}&language=ko-KR`
    })
    .then((response) => {
      movies.value = response.data.results.slice(0, 200)
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
      // const password = password1
      // logIn({ username, password })
    })
    .catch((error) => {
      console.log(error)
    })
  }

  return { movies, getMovies, signUp }
})
