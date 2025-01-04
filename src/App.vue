<template>
  <div id="app">
    <!-- Replace HelloWorld with QueryForm -->
    <QueryForm />
  </div>
</template>

<script>
import QueryForm from './components/QueryForm.vue'; // Import the new component

export default {
  name: 'App',
  components: {
    QueryForm, // Register the new component
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>

