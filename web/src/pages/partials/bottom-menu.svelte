<script>
  import Icon from 'svelte-icons-pack';
  import AiFillHome from "svelte-icons-pack/ai/AiFillHome";
  import FaSolidBook from 'svelte-icons-pack/fa/FaSolidBook';
  import IoBagHandle from "svelte-icons-pack/io/IoBagHandle";
  import BiSearchAlt from "svelte-icons-pack/bi/BiSearchAlt";
  import FaSolidUserCircle from 'svelte-icons-pack/fa/FaSolidUserCircle'
  import { inertia } from '@inertiajs/inertia-svelte';
</script>

<div class="fixed z-50 bg-white h-[75px] flex items-center bottom-0 w-full shadow-lg md:hidden">
  <nav class="flex flex-row justify-around items-center w-full">
    <a use:inertia href="/" class="flex flex-col gap-1 justify-center items-center">
      <Icon src={AiFillHome} size="27" className="fill-orange-600 group-hover:fill-orange-500"/>
    </a>
    <a use:inertia href="/books">
      <Icon src={FaSolidBook} size="24" className="fill-orange-600 group-hover:fill-orange-500"/>
    </a>
    <a use:inertia href="/search" class="p-3 bg-sky-700 rounded-full flex items-center justify-center">
      <Icon src={BiSearchAlt} size="25" className="fill-white"/>
    </a>
    <a use:inertia href="/peminjaman">
      <Icon src={IoBagHandle} size="28" className="fill-orange-600 group-hover:fill-orange-500"/>
    </a>
    <a use:inertia href="/profile">
      <Icon src={FaSolidUserCircle} size="26" className="fill-orange-600 group-hover:fill-orange-500"/>
    </a>
  </nav>
</div>