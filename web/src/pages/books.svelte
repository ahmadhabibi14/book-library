<script>
  import { inertia } from '@inertiajs/inertia-svelte';
  import Icon from 'svelte-icons-pack';
  import RiSystemLoader4Fill from 'svelte-icons-pack/ri/RiSystemLoader4Fill';
  import axios from 'axios';
  import { onMount } from 'svelte';
  import Growl from './components/growl.svelte';
  import {formatDate} from './components/xFormatter.js';

  export let title = 'Buku';

  let growl;
  let books = [], isLoadBook = false;
  let OFFSET = 0, LIMIT = 20;

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
</script>

<svelte:head>
  <title>{title} | Bacaku</title>
</svelte:head>

<Growl bind:this={growl} />
<div>
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
</div>