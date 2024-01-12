<script>
  import axios from 'axios';
  import { onMount } from 'svelte';
  import Growl from './components/growl.svelte';
  import XFormatter from './components/xFormatter.svelte';
  import Sidemenu from './partials/sidemenu.svelte';

  export let user = {};

  let growl, formatter;

  let books = [];
  let isLoadBook = false;
  async function getBooks() {
    isLoadBook = true;
    await axios.post('/api/books', {
      Headers: {
        'Content-Type': 'application/json'
      }
    }).then((res) => {
      isLoadBook = false;
      books = res.data.data;
      console.log(res.data.data)
    }).catch((err) => {
      isLoadBook = false;
      growl.showError(err.response.data.errors)
      console.log(err.response)
    })
  }

  onMount(async () => {
    await getBooks()
  });
</script>

<XFormatter bind:this={formatter} />
<Growl bind:this={growl} />

<div class="flex flex-row gap-10 justify-start">
  <div class="flex flex-col gap-6 w-fit">
    <h1 class="text-2xl text-orange-600 font-bold">Rekomendasi...</h1>
    <div class="grid grid-cols-5 gap-4">
      {#if books && books.length}
        {#each books as book}
          <a href="/" class="flex flex-col gap-2 w-40 p-3 bg-white rounded shadow group">
            <div class="w-full h-48 overflow-hidden rounded">
              <img src={book.thumbnail} alt="" class="hover:scale-110 w-full h-full object-cover duration-75"/>
            </div>
            <div class="flex flex-col gap-1">
              <span class="text-sm text-orange-600">{book.penulis}</span>
              <span class="text-base group-hover:underline">{book.judul}</span>
              <span class="font-light text-xs">{formatter.formatDate(book.rilis)}</span>
            </div>
          </a>
        {/each}
      {/if}
    </div>
    {#if isLoadBook}
      <div>Loading</div>
    {/if}
  </div>
  <Sidemenu {user} />
</div>

