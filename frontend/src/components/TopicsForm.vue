<template>
  <div class="topics-form">
    <h2>Core Topics</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="coreTopics">Core Topics (comma-separated)</label>
        <input
          type="text"
          id="coreTopics"
          v-model="formData.core_topics"
          class="form-control"
          placeholder="Enter topics separated by commas"
        />
      </div>
      <button type="submit" class="btn btn-primary">Save</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TopicsForm',
  data() {
    return {
      formData: {
        core_topics: '',
        input_hash: ''
      }
    };
  },
  mounted() {
    // Get input_hash from URL query params
    this.formData.input_hash = this.$route.query.input_hash;
    if (!this.formData.input_hash) {
      console.error('No input_hash provided in URL');
      return;
    }
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get(`http://localhost:3000/api/topics/${this.formData.input_hash}`);
        if (response.data) {
          this.formData.core_topics = response.data.core_topics.join(', ');
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    async handleSubmit() {
      try {
        const topics = this.formData.core_topics
          .split(',')
          .map(topic => topic.trim())
          .filter(topic => topic.length > 0);

        await axios.put(`http://localhost:3000/api/topics/${this.formData.input_hash}`, {
          core_topics: topics
        });
        alert('Topics updated successfully!');
      } catch (error) {
        console.error('Error updating topics:', error);
        alert('Error updating topics. Please try again.');
      }
    }
  }
};
</script>

<style scoped>
.topics-form {
  max-width: 600px;
  margin: 2rem auto;
  padding: 1rem;
}

.form-group {
  margin-bottom: 1rem;
}

.form-control {
  width: 100%;
  padding: 0.5rem;
  margin-top: 0.5rem;
}

.btn {
  padding: 0.5rem 1rem;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn:hover {
  background-color: #45a049;
}
</style> 