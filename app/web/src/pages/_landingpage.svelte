<script>
  import { inertia } from '@inertiajs/inertia-svelte';
  import { router } from '@inertiajs/svelte';
  import NProgress from 'nprogress';

  NProgress.configure({ easing: 'ease', speed: 500 });
  router.on('start', () => NProgress.start());
  router.on('finish', () => NProgress.done());

  export let title = '';
</script>

<svelte:head>
  <title>{title} | Bacaku</title>
</svelte:head>

<div class="w-full min-h-screen text-zinc-700 bg-white">
  <header class="h-16 w-full flex items-center justify-between px-28 shadow-lg">
    <a use:inertia href="/" class="hover:grayscale px-2 h-full flex items-center gap-2 font-bold text-2xl">
      <img src="/static/favicons/favicon.png" alt="" class="w-9 h-auto"/>
      <span>Bacaku</span>
    </a>
    <nav class="flex flex-row items-center gap-6 text-sky-700">
      <a use:inertia href="/about" class="text-lg hover:text-sky-600">
        Tentang
      </a>
      <a use:inertia href="/contact" class="text-lg hover:text-sky-600">
        Kontak
      </a>
      <a use:inertia href="/login" class="text-lg hover:text-sky-600">
        Login
      </a>
      <a use:inertia href="/register" class="text-lg hover:text-sky-600">
        Register
      </a>
    </nav>
  </header>
  <main class="min-h-screen px-28 pt-16">
    <div class="flex flex-row gap-14 items-center">
      <div class="w-[300px] h-auto shrink-0">
        <img src="static/img/woman-book.png" alt="" />
      </div>
      <div class="flex flex-col gap-3">
        <h1 class="text-5xl font-bold">Temukan buku favoritmu dan nikmati berbagai fitur menarik</h1>
        <a href="/login" class="bg-orange-400/10 text-orange-800 border-[2px] py-2 px-5 rounded-full border-orange-600 w-fit">
          Coba sekarang....
        </a>
      </div>
    </div>
  </main>
</div>