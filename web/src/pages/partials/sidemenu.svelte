<script>
  import Icon from 'svelte-icons-pack';
  import FaSolidBook from 'svelte-icons-pack/fa/FaSolidBook';
  import FaSolidMapMarkerAlt from 'svelte-icons-pack/fa/FaSolidMapMarkerAlt';

  export let user = {};
</script>

<aside class="w-[300px] bg-white p-5 rounded shadow h-fit flex flex-col gap-3">
  <h2 class="font-semibold text-lg pb-3 border-b border-zinc-300">{user.nama}</h2>
  <div class="flex flex-col gap-4">
    <div class="flex flex-col gap-1 text-sm">
      <div class="flex flex-row gap-2 items-center text-xs">
        <Icon size="11" src={FaSolidMapMarkerAlt} className="fill-orange-600" />
        <span>Alamat</span>
      </div>
      <span class="font-semibold">{user.alamat}</span>
    </div>
    <div class="flex flex-col gap-1 text-sm">
      <div class="flex flex-row gap-2 items-center text-xs">
        <Icon size="11" src={FaSolidBook} className="fill-orange-600" />
        <span>Buku yang dipinjam</span>
      </div>
      <span class="font-semibold">13 buku</span>
    </div>
  </div>
</aside>