<script>
  import Icon from 'svelte-icons-pack';
  import CgChevronRight from 'svelte-icons-pack/cg/CgChevronRight';
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

<div class="flex justify-center items-center h-screen w-full text-zinc-800">
  <div class="flex flex-col justify-center items-center gap-5">
    <h1 class="font-bold text-4xl">404 Page Not Found</h1>
    <a use:inertia href="/" class="flex flex-row bg-sky-700 hover:bg-sky-600 w-fit relative h-fit py-2 pl-5 pr-11 group rounded-full text-white">
      <span>Back to home</span>
      <Icon size="20" src={CgChevronRight} className="absolute right-4 group-hover:right-3 duration-150 h-full -mt-2"/>
    </a>
  </div>
</div>