<template>
	<div>
		<h4 class="margin-bot">{{review.movie.title}}</h4>
		<p>{{ review.content }}</p>
	</div>
</template>

<script setup>
defineProps({
  review: Object
})
</script>

<style scoped>
.margin-bot {
	font-size:20px;
	margin-bottom: 10px;
}
p{
	font-size: 14px;
		color: #333;
}
</style>