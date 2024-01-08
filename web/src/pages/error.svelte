<script>
  import { onMount } from "svelte";

  export let code = 400;
  export let status = '';
  export let message = '';

  onMount(() => {
    setTimeout(() => {
      window.location.href = '/login';
    }, 3000);
  })
</script>

<div>
  <h1>{code}</h1>
  <h2>{status}</h2>
  <p>{message}</p>
</div>