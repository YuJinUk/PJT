<template>
  <div class="article-list">
    <h3>Comments</h3>
    <input @click.keyup="">
    <button @click=""></button>
    <p
    v-for="comment in comments" :key="comment.id" :comment="comment"
    ></p>
  </div>
</template>

<script>
// import ArticleListItem from '@/components/ArticleListItem'

export default {
  name: 'Comment',
  components: {
    // ArticleListItem,
  },
  computed: {
    comments() {
      return this.$store.state.comments
    }
  }
}
</script>

<style>

</style>
