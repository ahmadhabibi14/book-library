<script>
  import { inertia } from '@inertiajs/inertia-svelte';
  import Icon from 'svelte-icons-pack';
  import FaSolidUserCircle from "svelte-icons-pack/fa/FaSolidUserCircle"
  import BsSearch from "svelte-icons-pack/bs/BsSearch";
  import IoNotifications from "svelte-icons-pack/io/IoNotifications";
  import Footer from './partials/footer.svelte';
</script>

<section class="w-full min-h-screen text-zinc-700 bg-zinc-100">
  <header class="px-28 w-full flex items-center justify-between fixed z-50 h-16 bg-white shadow-md">
    <div class="flex items-center gap-20 h-full">
      <a use:inertia href="/" class="hover:bg-zinc-100 px-2 h-full flex items-center gap-2 font-bold text-2xl">
        <img src="/static/favicons/favicon.png" alt="" class="w-9 h-auto"/>
        <span>ePerpus</span>
      </a>
      <nav class="flex items-center gap-6 text-lg font-semibold text-sky-700">
        <a href="/" class="hover:text-sky-600">Beranda</a>
        <a href="/" class="hover:text-sky-600">Buku</a>
        <a href="/" class="hover:text-sky-600">Peminjaman</a>
      </nav>
    </div>
    
    <div class="relative h-fit w-fit">
      <input
        type="text"
        class="bg-zinc-100 py-2 px-5 rounded-full w-96 focus:outline-none"
        placeholder="Cari buku, penulis ..."
      />
      <Icon src={BsSearch} size="16" className="absolute top-3 right-3 fill-zinc-500"/>
    </div>

    <div class="flex flex-row items-center gap-4">
      <a use:inertia href="/profile" class="flex font-semibold flex-row group items-center text-sm gap-2">
        <Icon src={IoNotifications} size="24" className="fill-orange-600 group-hover:fill-orange-500"/>
      </a>
      <a use:inertia href="/profile" class="flex font-semibold flex-row group items-center text-sm gap-2">
        <Icon src={FaSolidUserCircle} size="24" className="fill-orange-600 group-hover:fill-orange-500"/>
      </a>
    </div>
  </header>
  <main class="px-28 pt-24 pb-7">
    <slot />
  </main>
  <Footer />
</section>

<style>

</style>