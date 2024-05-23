<template>
  <tr>
    <td>{{ movie.movieNm }}</td>
    <td>{{ movie.director }}</td>
    <td>{{ movie.gradeNm }}</td>
    <p>{{ movie.actors }}</p>
  </tr>
</template>

<script setup>
const props = defineProps({
  movie: {
    type: Object,
    required: true
  }
})
</script>
<style scoped>
</style>
