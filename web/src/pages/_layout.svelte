<script>
  import { inertia } from '@inertiajs/inertia-svelte';
  import Icon from 'svelte-icons-pack';
  import FaSolidUserCircle from "svelte-icons-pack/fa/FaSolidUserCircle";
  import CgChevronRight from "svelte-icons-pack/cg/CgChevronRight";
</script>

<section class="w-full min-h-screen h-screen text-zinc-700 bg-zinc-100">
  <header class="px-28 w-full flex items-center justify-between sticky h-16 bg-white shadow-md">
    <div class="flex items-center gap-8 h-full">
      <a use:inertia href="/" class="hover:bg-zinc-100 px-2 h-full flex items-center gap-2 font-bold text-2xl">
        <img src="/static/favicons/favicon.png" alt="" class="w-9 h-auto"/>
        <span>ePerpus</span>
      </a>
      <nav></nav>
    </div>
    <div>
      <a use:inertia href="/profile" class="flex font-semibold flex-row group items-center text-sm gap-2">
        <Icon src={FaSolidUserCircle} size="30" className="fill-orange-600 group-hover:fill-orange-500"/>
      </a>
    </div>
  </header>
  <main class="px-28 pt-10">
    <slot />
  </main>
</section>

<style>

</style>