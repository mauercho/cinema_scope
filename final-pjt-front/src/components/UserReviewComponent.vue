<template>
	<div class="review">
		<div class="review-content">
		<h6>{{ review.user.username }}</h6>
		<p>{{ review.content }}</p>
		</div>
	</div>
</template>

<script setup>

defineProps({
	review: Object
})

</script>

<style scoped>
.reviews {
    margin-top: 20px;
}
.review {
    display: flex;
    flex-direction: column;
    margin-bottom: 10px;
}
.review-content {
    background-color: #f1f1f1;
    padding: 10px;
    border-radius: 8px;
    width: 100%;
}
h6 {
	margin: 0;
	font-weight: bold;
}
p {
	margin: 0;
}
</style>