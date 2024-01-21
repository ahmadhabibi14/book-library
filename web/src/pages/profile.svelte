<script>
  import Icon from 'svelte-icons-pack';
  import FaUserCircle from 'svelte-icons-pack/fa/FaUserCircle';
  import AiOutlineSetting from 'svelte-icons-pack/ai/AiOutlineSetting';
  import RiSystemLockPasswordLine from 'svelte-icons-pack/ri/RiSystemLockPasswordLine';
  import RiSystemLogoutBoxRLine from 'svelte-icons-pack/ri/RiSystemLogoutBoxRLine';
  import RiSystemLoader4Fill from 'svelte-icons-pack/ri/RiSystemLoader4Fill';
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

  let showLogoutPopup = false;
  function logout() {
    showLogoutPopup = true;
    var expiry = new Date(), cookieName = 'access_token';
    expiry.setTime(expiry.getTime() - 3600);
    document.cookie = cookieName + "=; expires=" + expiry.toUTCString() + "; path=/"
    setTimeout(()=> window.location.href = '/', 1200);
  }
</script>

<svelte:head>
  <title>{title} | ePerpus</title>
</svelte:head>

{#if showLogoutPopup}
  <div class="top-0 right-0 bottom-0 left-0 h-full w-full bg-zinc-950/30 flex justify-center fixed z-[99999]">
    <div class="bg-white w-[300px] flex flex-col justify-center items-center gap-2 p-5 rounded shadow-lg h-fit mt-24">
      <Icon size="40" src={RiSystemLoader4Fill} className="fill-sky-600 -mt-1 animate-spin" />
      <span>Loging out...</span>
    </div>
  </div>
{/if}
<div class="flex flex-row gap-5 relative">
  <div class="w-60 bg-white rounded p-5 flex flex-col gap-4 shadow sticky top-24">
    {#if MENU && MENU.length}
      {#each MENU as m}
        <button class="flex flex-row justify-between w-full items-center h-fit hover:underline" on:click={() => MODE = m.mode}>
          <div class="flex flex-row gap-3 items-center">
            <Icon size="22" src={m.icon} className="fill-orange-600 -mt-1" />
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
        <Icon size="22" src={RiSystemLogoutBoxRLine} className="fill-orange-600 -mt-1" />
        <span>Logout</span>
      </div>
    </button>
  </div>
  <div class="grow">
    {#if MODE === MODE_ACCOUNT}
    <div>
      Profil
    </div>
    {/if}
    {#if MODE === MODE_SETTINGS}
      <div>Pengaturan</div>
    {/if}
    {#if MODE === MODE_PASSWORD}
      <div>Ganti Password</div>
    {/if}
  </div>
</div>