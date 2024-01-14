<script>
  import Icon from 'svelte-icons-pack';
  import RiSystemShareBoxLine from "svelte-icons-pack/ri/RiSystemShareBoxLine";

  import { onMount } from 'svelte';
  import { formatDate } from './components/xFormatter.js';
  import { inertia } from '@inertiajs/inertia-svelte';

  export let title = '';

  /**
    * @typedef {Object} pinjam
    * @property {string} buku
    * @property {string} id
    * @property {string} slug
    * @property {string} tgl_kembali
    * @property {string} tgl_pinjam
    */
  /**
    * @type {Array<pinjam>}
    */
  export let peminjaman = [];

  onMount(() => {
    console.log('peminjaman', peminjaman)
  })
</script>

<svelte:head>
  <title>{title} | ePerpus</title>
</svelte:head>

<div>
  {#if peminjaman && peminjaman.length}
    <table class="w-full text-left text-sm shadow-md bg-white rounded-md overflow-hidden">
      <thead class="bg-sky-400/10 text-sky-700">
        <tr class="border-b border-sky-400/30">
          <th class="py-3 px-4 max-w-10">No</th>
          <th class="py-3 px-4">Buku</th>
          <th class="py-3 px-4">Tgl. Pinjam</th>
          <th class="py-3 px-4">Tgl. Kembali</th>
          <th class="py-3 px-4">Status</th>
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
            <button class="py-1 px-3 text-xs rounded-full bg-sky-700 hover:bg-sky-600 text-white">Kembalikan</button>
          </td>
        </tr>
      {/each}
      </tbody>
    </table>
  {/if}
</div>