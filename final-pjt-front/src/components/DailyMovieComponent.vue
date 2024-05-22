<template>
	<div>
		{{ movie.rank }}위: {{ movie.movieNm }}
		<hr>
	</div>
</template>

<script setup>
defineProps({
	movie: Object
})
</script>

<style scoped>

</style>