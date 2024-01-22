<script>
  import { inertia } from '@inertiajs/inertia-svelte';
  import { router } from '@inertiajs/svelte';
  import NProgress from 'nprogress';
  import { onMount } from 'svelte';
  import axios from 'axios';
  import Icon from 'svelte-icons-pack';
  import FaSolidUserCircle from 'svelte-icons-pack/fa/FaSolidUserCircle';
  import BsSearch from 'svelte-icons-pack/bs/BsSearch';
  import IoNotifications from 'svelte-icons-pack/io/IoNotifications';
  import FaSolidSwatchbook from 'svelte-icons-pack/fa/FaSolidSwatchbook';
  import Footer from './partials/footer.svelte';
  import BottomMenu from './partials/bottom-menu.svelte';
  
  let path = '/';
  $: path = window.location.pathname;
  NProgress.configure({ easing: 'ease', speed: 500 });

  router.on('start', () => NProgress.start());
  router.on('finish', () => {
    NProgress.done()
    path = window.location.pathname;
  });

  let notifTotal = 0;
  async function getTotalNotifikasi() {
    await axios.post('/api/total-notifikasi',
      {Headers: { 'Content-Type': 'application/json' }}
    ).then((res) => {
      notifTotal = res.data.data.total_notifikasi;
    }).catch((err) => {
      console.log(err.response);
    })
  }

  onMount( async ()=> await getTotalNotifikasi());

  function enterSearchInput(e) {
		if (e.key == 'Enter') window.location.href = '/search?query=' + e.target.value;
	}
</script>

<section class="w-full min-h-screen text-zinc-700 bg-zinc-50">
  <header class="w-full md:fixed z-50 h-16 md:bg-white md:shadow-md">
    <div class="container mx-auto px-1 md:px-4 lg:max-w-7xl flex h-full items-center justify-between">
      <div class="flex items-center gap-20 h-full">
        <a on:click={() => path = '/'} use:inertia href="/" class="hover:bg-zinc-100 px-2 h-full flex items-center gap-2 font-bold text-2xl">
          <img src="/static/favicons/favicon.png" alt="" class="w-9 h-auto"/>
          <span>Bacaku</span>
        </a>
        <nav class="hidden md:flex items-center gap-6 text-lg font-semibold text-sky-700 h-full">
          <a on:click={() => path = '/'} use:inertia href="/" class="hover:text-sky-600 relative h-full w-fit flex items-center">
            <span>Beranda</span>
            {#if path === '/'}
              <span class="absolute h-[3px] w-full flex justify-center bottom-2">
                <span class="bg-orange-600  rounded-full h-[3px] w-[50px]"></span>
              </span>
            {/if}
          </a>
          <a on:click={() => path = '/books'} use:inertia href="/books" class="hover:text-sky-600 relative h-full w-fit flex items-center">
            <span>Buku</span>
            {#if path === '/books'}
              <span class="absolute h-[3px] w-full flex justify-center bottom-2">
                <span class="bg-orange-600  rounded-full h-[3px] w-[50px]"></span>
              </span>
            {/if}
          </a>
          <a on:click={() => path = '/peminjaman'} use:inertia href="/peminjaman" class="hover:text-sky-600 relative h-full w-fit flex items-center">
            <span>Peminjaman</span>
            {#if path === '/peminjaman'}
              <span class="absolute h-[3px] w-full flex justify-center bottom-2">
                <span class="bg-orange-600  rounded-full h-[3px] w-[50px]"></span>
              </span>
            {/if}
          </a>
        </nav>
      </div>
      <div class="hidden md:block relative h-fit w-fit">
        <input
          on:keydown={enterSearchInput}
          type="text"
          class="bg-zinc-100 py-2 px-5 rounded-full w-96 focus:outline-none"
          placeholder="Cari buku ..."
        />
        <Icon src={BsSearch} size="16" className="absolute top-3 right-3 fill-zinc-500"/>
      </div>
      <div class="flex flex-row items-center gap-4 mr-4 md:mr-0">
        <a use:inertia href="/notifikasi" class="relative flex font-semibold flex-row group items-center text-sm gap-2">
          <Icon src={IoNotifications} size="24" className="fill-orange-600 group-hover:fill-orange-500"/>
          {#if notifTotal > 0}
            <span class="absolute flex justify-center items-center -top-1 -right-1 leading-none text-[8px] bg-sky-700 rounded-full py-[3px] px-[5px] text-white h-fit w-fit">
              <p>{notifTotal}</p>
            </span>
          {/if}
        </a>
        <a use:inertia href="/koleksi" class="flex font-semibold flex-row group items-center text-sm gap-2">
          <Icon src={FaSolidSwatchbook} size="20" className="fill-orange-600 group-hover:fill-orange-500"/>
        </a>
        <a use:inertia href="/profile" class="hidden md:flex font-semibold flex-row group items-center text-sm gap-2">
          <Icon src={FaSolidUserCircle} size="24" className="fill-orange-600 group-hover:fill-orange-500"/>
        </a>
      </div>
    </div>
  </header>
  <main class="container lg:max-w-7xl px-4 mx-auto pt-4 md:pt-24 pb-24 min-h-[95vh]">
    <slot />
  </main>
  <Footer />
  <BottomMenu />
</section>

<style>

</style>