<script>
  import Icon from 'svelte-icons-pack';
  import BsSearch from 'svelte-icons-pack/bs/BsSearch';
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

  let query = '';
  function searchBook() {
    window.location.href = '/search?query=' + query;
  }
  function enterSearchInput(e) {
		if (e.key == 'Enter') window.location.href = '/search?query=' + e.target.value;
	}
</script>

<svelte:head>
  <title>{title} | ePerpus</title>
</svelte:head>

<div class="flex flex-col gap-4">
  <div class="flex md:hidden">
    <div class="relative h-fit w-full text-zinc-800">
      <input
        bind:value={query}
        on:keydown={enterSearchInput}
        type="text"
        class="bg-zinc-100 py-2 pl-4 md:pl-6 pr-10 rounded-full w-full focus:outline-none"
        placeholder="Cari buku ..."
      />
      <button class="absolute top-3 md:top-4 right-3 md:right-4" on:click={searchBook}>
        <Icon src={BsSearch} size="18" className=" fill-orange-600"/>
      </button>
    </div>
  </div>
  <h1 class="text-lg md:text-xl">Hasil pencarian buku dengan kata kunci <span class="text-orange-600">"{queryParamValue}"</span></h1>
  <div class="flex flex-col gap-6 w-fit">
    <div class="md:grid flex flex-wrap md:grid-cols-5 gap-4 justify-between md:gap-4">
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