<template>
	<div class="mt-2 mb-2">
		{{ movie.rank }}위: {{ movie.movieNm }}
	</div>
</template>

<script setup>
defineProps({
	movie: Object
})
</script>

<style scoped>

</style>

