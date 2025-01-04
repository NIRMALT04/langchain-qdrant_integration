<template>
    <div class="query-form">
      <h1>Query App</h1>
      <form @submit.prevent="submitQuery">
        <input
          v-model="query"
          type="text"
          placeholder="Enter your query"
          required
        />
        <button type="submit">Submit</button>
      </form>
      <div v-if="response">
        <h2>Response:</h2>
        <p>{{ response }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        query: "",
        response: null,
      };
    },
    methods: {
      async submitQuery() {
        try {
          const res = await axios.post("http://localhost:5000/query", {
            query: this.query,
          });
          this.response = res.data.answer; // Adjust according to API response structure
        } catch (err) {
          console.error(err);
          this.response = "Error: Unable to fetch response";
        }
      },
    },
  };
  </script>
  
  <style>
  .query-form {
    max-width: 600px;
    margin: 50px auto;
    text-align: center;
  }
  input {
    width: 80%;
    padding: 10px;
    margin-bottom: 10px;
  }
  button {
    padding: 10px 20px;
  }
  </style>
  