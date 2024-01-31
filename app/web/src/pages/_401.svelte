<script>
  import { onMount } from 'svelte';

  export let code = 401;
  export let status = '';
  export let message = '';

  let title = '401 Unauthorized Access';

  onMount(() => {
    document.cookie = `access_token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
  })
</script>

<svelte:head>
  <title>{title}</title>
</svelte:head>

<div class="flex flex-col items-center w-96 mt-16 mx-auto">
  <h1>{code}</h1>
  <h2>{status}</h2>
  <p>{message}</p>
  <a href="/login" class="py-2 px-5 bg-sky-700 text-white">Go to login</a>
</div>