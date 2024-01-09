<script>
  export let user = {};
  console.log('user', user);
</script>

<div>
  <h1>Hello world !!</h1>
  {#if user}
    <ul>
      <li>Nama: {user.nama}</li>
      <li>Email: {user.email}</li>
      <li>Telepon: {user.telepon}</li>
      <li>Alamat: {user.alamat}</li>
      <li>Jenis Kelamin: {user.jenis_kelamin}</li>
    </ul>
  {/if}
</div>

