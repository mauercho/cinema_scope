<template>
	<div>
		<div class="card">
			<div class="card-header">
				{{ review.user.username }}
			</div>
			<div class="card-body">
				<blockquote class="blockquote mt-3">
					<p>{{ review.content }}</p>
				</blockquote>
			</div>
		</div>
	</div>
</template>

<script setup>

defineProps({
	review: Object
})

</script>

<style scoped>
.card {
	width: 500px;
	height: auto;
}
</style>