<script>
  import { onMount } from 'svelte';
  import { inertia } from '@inertiajs/inertia-svelte';
  import { formatDate } from './components/xFormatter';

  export let title = '';
  export let books = [];

  let searchParams = new URLSearchParams(location.search);
  let queryParamValue = searchParams.get('query') || '';

  onMount(() => {
    console.log(books);
  })
</script>

<svelte:head>
  <title>{title} | ePerpus</title>
</svelte:head>

<div class="flex flex-col gap-4">
  <h1 class="text-xl">Hasil pencarian buku dengan kata kunci <span class="text-orange-600">"{queryParamValue}"</span></h1>
  <div class="flex flex-col gap-6 w-fit">
    <div class="grid grid-cols-7 gap-4">
      {#if books && books.length}
        {#each books as book}
          <a use:inertia href={'books/'+book.slug} class="flex flex-col gap-2 w-40 p-3 bg-white rounded shadow group">
            <div class="w-full h-48 overflow-hidden rounded">
              <img src={book.thumbnail} alt="" class="hover:scale-110 hover:grayscale w-full h-full object-cover duration-75"/>
            </div>
            <div class="flex flex-col gap-1">
              <span class="truncate text-sm text-orange-600">{book.penulis}</span>
              <span class="truncate text-base group-hover:underline">{book.judul}</span>
              <span class="font-light text-xs">{formatDate(book.rilis)}</span>
            </div>
          </a>
        {/each}
      {/if}
    </div>
  </div>
</div>