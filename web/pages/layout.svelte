<script>
  import { inertia } from '@inertiajs/svelte'
</script>

<main>
  <header>
    <a use:inertia href="/">Home</a>
    <a use:inertia href="/login">Login</a>
  </header>
  <article>
    <slot />
  </article>
</main>