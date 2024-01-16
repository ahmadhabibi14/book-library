<script>
  import Icon from 'svelte-icons-pack';
  import FaUserCircle from 'svelte-icons-pack/fa/FaUserCircle';
  import AiOutlineSetting from 'svelte-icons-pack/ai/AiOutlineSetting';
  import RiSystemLockPasswordLine from 'svelte-icons-pack/ri/RiSystemLockPasswordLine';
  import RiSystemLogoutBoxRLine from 'svelte-icons-pack/ri/RiSystemLogoutBoxRLine';
  export let title = '';

  const MODE_ACCOUNT = `account`, MODE_SETTINGS = `settings`, MODE_PASSWORD = `password`;
  let MODE = MODE_ACCOUNT;

  const MENU = [
    {
      mode: MODE_ACCOUNT,
      icon: FaUserCircle,
      title: 'Profil Saya',
    },
    {
      mode: MODE_SETTINGS,
      icon: AiOutlineSetting,
      title: 'Pengaturan',
    },
    {
      mode: MODE_PASSWORD,
      icon: RiSystemLockPasswordLine,
      title: 'Ganti Password',
    }
  ]

  function logout() {
    console.log('logout');
  }
</script>

<svelte:head>
  <title>{title} | ePerpus</title>
</svelte:head>

<div class="flex flex-row gap-5 relative">
  <div class="text-sm w-60 bg-white rounded p-5 flex flex-col gap-4 shadow sticky top-24">
    {#if MENU && MENU.length}
      {#each MENU as m}
        <button class="flex flex-row justify-between w-full items-centerh-fit hover:underline" on:click={() => MODE = m.mode}>
          <div class="flex flex-row gap-3 items-center">
            <Icon size="18" src={m.icon} className="fill-orange-600 -mt-1" />
            <span>{m.title}</span>
          </div>
          {#if MODE === m.mode}
            <span class="bg-orange-600 h-[15px] w-[3px] rounded-full"></span>
          {/if}
        </button>
      {/each}
    {/if}
    <button class="flex flex-row justify-between w-full items-centerh-fit hover:underline" on:click={logout}>
      <div class="flex flex-row gap-3 items-center">
        <Icon size="18" src={RiSystemLogoutBoxRLine} className="fill-orange-600 -mt-1" />
        <span>Logout</span>
      </div>
    </button>
  </div>
  <div class="grow">
    <p>Haloo</p>
  </div>
</div>