<script>
  import Icon from 'svelte-icons-pack';
  import FaSolidBook from 'svelte-icons-pack/fa/FaSolidBook';
  import FaSolidMapMarkerAlt from 'svelte-icons-pack/fa/FaSolidMapMarkerAlt';
  import IoHelpCircle from 'svelte-icons-pack/io/IoHelpCircle';
  import FaCalendarAlt from 'svelte-icons-pack/fa/FaCalendarAlt';

  import {formatDate} from '../components/xFormatter.js';
  import { inertia } from '@inertiajs/inertia-svelte';

  export let user = {};
</script>

<aside class="w-full md:w-[300px] flex flex-col gap-4 md:sticky top-24 h-fit">
  <div class="bg-orange-100 text-orange-900 p-5 rounded shadow h-fit flex flex-col gap-3">
    <h2 class="font-semibold text-lg pb-3 border-b border-orange-300">{user.nama}</h2>
    <div class="flex flex-col gap-4">
      <div class="flex flex-col gap-1 text-sm">
        <div class="flex flex-row gap-2 items-center text-xs">
          <Icon size="11" src={FaSolidMapMarkerAlt} className="fill-orange-600 -mt-1" />
          <span>Alamat</span>
        </div>
        <span class="font-semibold">{user.alamat}</span>
      </div>
      <div class="flex flex-col gap-1 text-sm">
        <div class="flex flex-row gap-2 items-center text-xs">
          <Icon size="11" src={FaCalendarAlt} className="fill-orange-600 -mt-1" />
          <span>Bergabung pada</span>
        </div>
        <span class="font-semibold">{formatDate(user.join_at)}</span>
      </div>
      <div class="flex flex-col gap-1 text-sm">
        <div class="flex flex-row gap-2 items-center text-xs">
          <Icon size="11" src={FaSolidBook} className="fill-orange-600 -mt-1" />
          <span>Buku yang dipinjam</span>
        </div>
        <span class="font-semibold">{user.total_peminjaman} buku</span>
      </div>
    </div>
  </div>
  <a use:inertia href="/help" class="bg-sky-700 hover:bg-sky-600 text-white py-2 px-5 rounded text-center w-full flex flex-row items-center gap-1 justify-center">
    <Icon size="17" src={IoHelpCircle} className="fill-white -mt-1" />
    <span>Pusat bantuan</span>
  </a>
</aside>