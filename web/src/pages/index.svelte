<script>
  export let anggota = [];
  console.log('anggota', anggota);
</script>

<div>
  <h1>Hello world !!</h1>
  {#if anggota && anggota.length}
    {#each anggota as anggota}
      <ul>
        <li>Nama: {anggota.nama}</li>
        <li>Email: {anggota.email}</li>
        <li>Telepon: {anggota.telepon}</li>
        <li>Alamat: {anggota.alamat}</li>
        <li>Jenis Kelamin: {anggota.jenis_kelamin}</li>
      </ul>
    {/each}
  {/if}
</div>

