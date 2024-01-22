<script>
  import Icon from 'svelte-icons-pack';
  import IoBagHandle from 'svelte-icons-pack/io/IoBagHandle';
  import RiSystemLoader4Fill from 'svelte-icons-pack/ri/RiSystemLoader4Fill';
  import { onMount } from 'svelte';
  import { formatDate } from './components/xFormatter.js';
  import Growl from './components/growl.svelte';
  import axios from 'axios';

  export let book = {};
  let title = 'Book';
  let growl, deskripsi = '';

  onMount(() => {
    if (book.deskripsi) {
      deskripsi = book.deskripsi;
      title = `${book.judul}`;
    }
  })

  let isPinjamBuku = false;
  async function pinjamBuku() {
    isPinjamBuku = true;
    await axios({
      method: 'post',
      url: '/api/pinjam-buku',
      data: { buku_id: book.id },
      headers: { 'Content-Type': 'application/json' },
    }).then((res) => {
      isPinjamBuku = false;
      console.log(res.data);
      growl.showSuccess(res.data.message);
    }).catch((err) => {
      isPinjamBuku = false;
      growl.showError(err.response.data.message)
      console.log(err.response);
    })
  }
</script>

<svelte:head>
  <title>{title} | Bacaku</title>
</svelte:head>

<Growl bind:this={growl} />
<div>
  {#if Object.keys(book).length === 0}
    <div class="flex flex-col mt-16 gap-7 justify-center items-center w-full">
      <div class="w-[310px]">
        <img src="/static/img/no-book.png" alt="" />
      </div>
      <h1 class="font-bold text-zinc-300 text-3xl">Buku tidak ditemukan !!</h1>
    </div>
  {/if}
  {#if Object.keys(book).length !== 0}
    <div class="grid grid-cols-4 gap-10 relative">
      <div class="col-span-1 flex flex-col gap-4 items-end h-fit sticky top-24">
        <div class="cursor-pointer w-60 h-80 overflow-hidden rounded border border-zinc-200 shadow">
          <img src={book.thumbnail} alt="" class="hover:scale-110 hover:grayscale w-full h-full object-cover duration-75"/>
        </div>
      </div>
      <div class="col-span-2 flex flex-col gap-6">
        <div class="flex flex-col gap-1">
          <span class="text-orange-600">{book.penulis}</span>
          <h1 class="text-3xl font-bold">{book.judul}</h1>
          <span class="text-xs text-zinc-600">Terbit: {formatDate(book.rilis)}</span>
        </div>
        <p class="text-sm font-normal">{@html deskripsi.replace(/\r\n|\n|\r/gm, '<br />')}</p>
      </div>
      <aside class="col-span-1 h-fit sticky top-24">
        <button on:click={pinjamBuku} class="bg-sky-700 hover:bg-sky-600 text-white py-2 px-5 rounded text-center w-full flex flex-row items-center gap-2 justify-center">
          {#if !isPinjamBuku}
            <Icon size="14" src={IoBagHandle} className="fill-white -mt-1" />
          {/if}
          {#if isPinjamBuku}
            <Icon size="14" src={RiSystemLoader4Fill} className="fill-white -mt-1 animate-spin" />
          {/if}
          <span>Pinjam buku ini</span>
        </button>
      </aside>
    </div>
  {/if}
</div>