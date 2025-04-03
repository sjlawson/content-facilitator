<template>
  <div id="app">
    <TopicsForm />
  </div>
</template>

<script>
import TopicsForm from './components/TopicsForm.vue'

export default {
  name: 'App',
  components: {
    TopicsForm
  }
}
</script>

<style>
#app {
  font-family: Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin-top: 60px;
}
</style> 