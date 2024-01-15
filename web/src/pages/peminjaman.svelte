<script>
  import Icon from 'svelte-icons-pack';
  import RiSystemShareBoxLine from "svelte-icons-pack/ri/RiSystemShareBoxLine";
  import RiSystemLoader4Fill from 'svelte-icons-pack/ri/RiSystemLoader4Fill';

  import { onMount } from 'svelte';
  import { formatDate } from './components/xFormatter.js';
  import { inertia } from '@inertiajs/inertia-svelte';
  import axios from 'axios';
  import Growl from './components/growl.svelte';

  export let title = '';

  /**
    * @typedef {Object} pinjam
    * @property {string} buku
    * @property {string} id
    * @property {string} slug
    * @property {string} tgl_kembali
    * @property {string} tgl_pinjam
    * @property {string} dikembalikan
    */
  /**
    * @type {Array<pinjam>}
    */
  export let peminjaman = [];
  let growl;

  onMount(() => {
    console.log('peminjaman', peminjaman)
  })

  let isSubmitKembalikan = false;
  async function kembalikanBuku() {
    isSubmitKembalikan = true;
    await axios.post('/api/kembalikan-buku', {
      Headers: { 'Content-Type': 'application/json' }
    }).then((res) => {
      isSubmitKembalikan = false;
      growl.showSuccess(res.data.message)
      setTimeout(() => {
        window.location.reload();
      }, 1300)
    }).catch((err) => {
      isSubmitKembalikan = false;
      growl.showError(err.response.data.errors)
      console.log(err.response)
    })
  }
</script>

<svelte:head>
  <title>{title} | ePerpus</title>
</svelte:head>

<Growl bind:this={growl} />

<div>
  {#if peminjaman && peminjaman.length}
    <table class="w-full text-left text-sm shadow-md bg-white rounded-md overflow-hidden">
      <thead class="bg-sky-400/10 text-sky-700">
        <tr class="border-b border-sky-400/30">
          <th class="py-3 px-4 max-w-10">No</th>
          <th class="py-3 px-4">Buku</th>
          <th class="py-3 px-4">Tgl. Pinjam</th>
          <th class="py-3 px-4">Tgl. Kembali</th>
          <th class="py-3 px-4 flex flex-row gap-2 items-center">
            <span>Status</span>
            {#if isSubmitKembalikan}
              <Icon size="14" src={RiSystemLoader4Fill} className="fill-sky-600 -mt-1 animate-spin" />
            {/if}
          </th>
        </tr>
      </thead>
      <tbody>
      {#each peminjaman as pinjam, idx}
        <tr>
          <td class="py-3 px-4 max-w-10 font-semibold">{idx+1}</td>
          <td class="py-3 px-4">
            <a use:inertia href="/books/{pinjam.slug}" class="flex flex-row gap-1 hover:underline">
              <span>{pinjam.buku}</span>
              <Icon src={RiSystemShareBoxLine} size="13" className="fill-sky-600"/>
            </a>
          </td>
          <td class="py-3 px-4">{formatDate(pinjam.tgl_pinjam)}</td>
          <td class="py-3 px-4">{formatDate(pinjam.tgl_kembali)}</td>
          <td class="py-3 px-4">
            {#if pinjam.dikembalikan}
              <span>Dikembalikan</span>
            {/if}
            {#if !pinjam.dikembalikan}
              <button on:click={kembalikanBuku} class="py-1 px-3 text-xs rounded-full bg-sky-700 hover:bg-sky-600 text-white">
                Kembalikan
              </button>
            {/if}
          </td>
        </tr>
      {/each}
      </tbody>
    </table>
  {:else}
  <div class="flex flex-col mt-16 gap-7 justify-center items-center w-full">
    <div class="w-[310px]">
      <img src="/static/img/woman-book-2.png" alt="" />
    </div>
    <h1 class="font-bold text-zinc-300 text-3xl">Belum ada buku yang dipinjam !!</h1>
  </div>
  {/if}
</div>