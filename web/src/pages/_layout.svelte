<script>
  import { inertia } from '@inertiajs/inertia-svelte'
</script>

<section>
  <nav>
    <a use:inertia href="/" class="current">Home</a>
    <a use:inertia href="/about">About</a>
  </nav>
  <main>
    <slot />
  </main>
</section>
