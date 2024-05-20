<template>
	<div>

	</div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useMovieStore } from '@/stores/counter'
import { useRouter } from 'vue-router'

const store = useMovieStore()
const router = useRouter()

onMounted(() => {
	store.logOut()
	router.push({ name : 'home' })
})
</script>

<style scoped>

</style>