<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Answer from "./routes/Answer.svelte"

  const routes = {
    '/':Home,
    '/answer':Answer,
  }
  
</script>

<Router {routes}/>