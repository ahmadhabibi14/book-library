<script>
  import Icon from 'svelte-icons-pack/Icon.svelte';
  import IoClose from 'svelte-icons-pack/io/IoClose';
  import FaCalendarAlt from 'svelte-icons-pack/fa/FaCalendarAlt';
  import { onMount } from 'svelte';
  import { formatTime } from './components/xFormatter';
  import { writable } from 'svelte/store';
  import axios from 'axios';

  export let title = '';
  /**
    * @typedef {Object} notif
    * @property {string} id
    * @property {string} pesan
    * @property {Date} tanggal
    * @property {boolean} dibaca
    */
  /** @type {Array<notif>} */
  export let notifikasi = [];
  let W_notifikasi = writable(notifikasi);

  onMount(() => $W_notifikasi = notifikasi);

  const updateNotifikasi = function(/** @type {string} */ id) {
    let not = $W_notifikasi;
    for (var i in not) if (not[i].id === id) not[i].dibaca = true;
    return not
  }

  async function hapusNotifikasi(/** @type {string} */id) {
    await axios({
      method: 'post',
      url: '/api/hapus-notifikasi',
      data: { notifikasi_id: id },
      headers: { 'Content-Type': 'application/json' }
    }).then((res) => {
      console.log(res.data);
      $W_notifikasi = updateNotifikasi(id);
    }).catch((err) => {
      console.log(err.response)
    })
  }
</script>

<svelte:head>
  <title>{title} | Bacaku</title>
</svelte:head>

<div>
  <div class="max-w-[600px] mx-auto flex flex-col gap-4">
    {#if $W_notifikasi && $W_notifikasi.length}
      {#each $W_notifikasi as n}
        <div class={`border flex flex-row justify-start gap-2 w-full py-2 px-3 rounded ${n.dibaca ? 'bg-zinc-100 border-zinc-200' : 'bg-sky-400/10 border-sky-500'}`}>
          <div class="flex flex-col gap-1 grow">
            <h5 class={`text-base ${n.dibaca ? 'text-zinc-500' : 'text-sky-700'}`}>{n.pesan}</h5>
            <div class="flex flex-row gap-2 items-center text-sm">
              <Icon size="11" src={FaCalendarAlt} className="fill-sky-800 -mt-1" />
              <span>{formatTime(n.tanggal)}</span>
            </div>
          </div>
          {#if !n.dibaca}
            <button
              title="Tandai telah dibaca"
              class="w-fit h-fit p-1 hover:bg-sky-500/20 rounded-full"
              on:click={()=>hapusNotifikasi(n.id)}>
              <Icon title="Tandai telah dibaca" size="17" className="fill-sky-800" src={IoClose}/>
            </button>
          {/if}
        </div>
      {/each}
    {:else}
      <div class="text-center flex justify-center">
        <div class="text-zinc-400 text-2xl font-bold flex flex-row gap-5 items-center mt-6">
          <div class="w-[80px]">
            <img src="/static/img/notification.png" alt="" />
          </div>
          <h1>Tidak ada notifikasi !!</h1>
        </div>
      </div>
    {/if}
  </div>
</div>