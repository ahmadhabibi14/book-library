<script>
  import { inertia } from '@inertiajs/inertia-svelte';
  import Icon from 'svelte-icons-pack';
  import RiSystemLoader4Fill from 'svelte-icons-pack/ri/RiSystemLoader4Fill';
  import BsSearch from 'svelte-icons-pack/bs/BsSearch';
  import axios from 'axios';
  import { onMount } from 'svelte';
  import Growl from './components/growl.svelte';
  import {formatDate} from './components/xFormatter.js';
  import Sidebar from './partials/sidebar.svelte';

  export let user = {};
  export let title = '';

  let growl, books = [], isLoadBook = false;
  let OFFSET = 0, LIMIT = 10;

  async function getBooks() {
    isLoadBook = true;
    await axios.post('/api/books?offset='+OFFSET+'&limit='+LIMIT, {
      Headers: { 'Content-Type': 'application/json' }
    }).then((res) => {
      isLoadBook = false;
      if (!books.length) {
        OFFSET += LIMIT;
        books = res.data.data;
      } else {
        OFFSET += LIMIT;
        const DATA = res.data.data;
        books = [...books, ...DATA];
      }
    }).catch((err) => {
      isLoadBook = false;
      growl.showError(err.response.data.errors)
      console.log(err.response)
    })
  }

  onMount(async () => await getBooks());

  const init = (/** @type {HTMLInputElement} */ el) => el.focus();
  function enterSearchInput(/** @type {any} */ e) {
		if (e.key == 'Enter') window.location.href = '/search?query=' + e.target.value;
	}
  let inputSearch = '';
  const searchBook = () => window.location.href = '/search?query=' + inputSearch;
</script>

<svelte:head>
  <title>{title} | Bacaku</title>
</svelte:head>

<Growl bind:this={growl} />

<div class="flex flex-col gap-6 md:gap-8">
  <div class="relative">
    <header class="flex flex-col w-full justify-center items-center h-full gap-4 md:gap-9 absolute text-white mx-auto">
      <h1 class="drop-shadow-2xl text-xl md:text-5xl font-semibold text-center w-10/12 md:w-3/5 mx-auto">
        Temukan buku favoritmu dan nikmati berbagai fitur menarik
      </h1>
      <div>
        <div class="relative h-fit w-fit text-zinc-800">
          <input
            bind:value={inputSearch}
            on:keydown={enterSearchInput}
            use:init
            type="text"
            class="bg-zinc-100 py-2 md:py-3 pl-4 md:pl-6 pr-16 rounded-full w-[300px] md:w-[500px] focus:outline-none"
            placeholder="Cari buku ..."
          />
          <button
            on:click={searchBook}
            class="flex justify-center items-center py-[6px] md:py-2 px-3 md:px-4 rounded-full bg-orange-600 hover:bg-orange-500 h-fit w-fit absolute top-[5px] md:top-[7px] right-[6px] md:right-2">
            <Icon src={BsSearch} size="18" className=" fill-white"/>
          </button>
        </div>
      </div>
    </header>
    <div class="w-full h-[180px] md:h-[400px] rounded-lg overflow-hidden">
      <img src="/static/img/book-lib.jpg" alt="" />
    </div>
  </div>
  <div class="flex flex-col-reverse md:flex-row gap-5 md:gap-10 justify-between relative">
    <div class="flex flex-col gap-5 md:gap-6 w-fit">
      <h1 class="text-2xl text-orange-600 font-bold">Rekomendasi...</h1>
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
      <div class="flex justify-center text-sm">
        {#if isLoadBook}
          <div class="flex flex-row items-center gap-2">
            <Icon size="14" src={RiSystemLoader4Fill} className="fill-orange-600 -mt-1 animate-spin" />
            <span>Loading more</span>
          </div>
        {/if}
        {#if !isLoadBook}
          <button on:click={getBooks} class="text-orange-600 bg-white shadow py-2 px-5 rounded hover:bg-zinc-50">Load more</button>
        {/if}
      </div>
    </div>
    <Sidebar {user} />
  </div>
</div>
