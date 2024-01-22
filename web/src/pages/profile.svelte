<script>
  import Icon from 'svelte-icons-pack';
  import FaUserCircle from 'svelte-icons-pack/fa/FaUserCircle';
  import AiOutlineSetting from 'svelte-icons-pack/ai/AiOutlineSetting';
  import RiSystemLockPasswordLine from 'svelte-icons-pack/ri/RiSystemLockPasswordLine';
  import RiSystemLogoutBoxRLine from 'svelte-icons-pack/ri/RiSystemLogoutBoxRLine';
  import RiSystemLoader4Fill from 'svelte-icons-pack/ri/RiSystemLoader4Fill';
  import RiDesignBallPenLine from 'svelte-icons-pack/ri/RiDesignBallPenLine';
  import Inputbox from './components/inputbox.svelte';

  export let title = '';
  export let user = {};

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

  let oldPassword = '', newPassword = '', newPasswordConfirm = '';
</script>

<svelte:head>
  <title>{title} | Bacaku</title>
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
  <div class="h-fit w-72 bg-white rounded p-5 flex flex-col gap-4 shadow sticky top-24">
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
    <div class="flex flex-col gap-4 p-5 bg-white rounded shadow">
      <div class="flex flex-row gap-4 items-center">
        <div class="grow flex flex-col gap-1">
          <span class="text-xs text-orange-600">Nama</span>
          <p>{user.nama}</p>
        </div>
        <button title="Edit nama" class="w-fit p-2 hover:bg-zinc-100 active:bg-zinc-200 rounded-full flex h-fit items-center justify-center">
          <Icon size="16" src={RiDesignBallPenLine} className="fill-orange-600" />
        </button>
      </div>
      <div class="flex flex-row gap-4 items-center">
        <div class="grow flex flex-col gap-1">
          <span class="text-xs text-orange-600">Alamat</span>
          <p>{user.alamat}</p>
        </div>
        <button title="Edit alamat" class="w-fit p-2 hover:bg-zinc-100 active:bg-zinc-200 rounded-full flex h-fit items-center justify-center">
          <Icon size="16" src={RiDesignBallPenLine} className="fill-orange-600" />
        </button>
      </div>
      <div class="flex flex-row gap-4 items-center">
        <div class="grow flex flex-col gap-1">
          <span class="text-xs text-orange-600">Email</span>
          <p>{user.email}</p>
        </div>
        <button title="Edit email" class="w-fit p-2 hover:bg-zinc-100 active:bg-zinc-200 rounded-full flex h-fit items-center justify-center">
          <Icon size="16" src={RiDesignBallPenLine} className="fill-orange-600" />
        </button>
      </div>
      <div class="flex flex-row gap-4 items-center">
        <div class="grow flex flex-col gap-1">
          <span class="text-xs text-orange-600">No. Telepon</span>
          <p>{user.telepon}</p>
        </div>
        <button title="Edit No. Telepon" class="w-fit p-2 hover:bg-zinc-100 active:bg-zinc-200 rounded-full flex h-fit items-center justify-center">
          <Icon size="16" src={RiDesignBallPenLine} className="fill-orange-600" />
        </button>
      </div>
      <div class="flex flex-row gap-4 items-center">
        <div class="grow flex flex-col gap-1">
          <span class="text-xs text-orange-600">Jenis Kelamin</span>
          <p>{user.jenis_kelamin === 'L' ? 'Laki - Laki' : 'Perempuan'}</p>
        </div>
        <button title="Edit Jenis Kelamin" class="w-fit p-2 hover:bg-zinc-100 active:bg-zinc-200 rounded-full flex h-fit items-center justify-center">
          <Icon size="16" src={RiDesignBallPenLine} className="fill-orange-600" />
        </button>
      </div>
    </div>
    {/if}
    {#if MODE === MODE_SETTINGS}
      <div>Pengaturan</div>
    {/if}
    {#if MODE === MODE_PASSWORD}
      <div class="flex flex-col gap-4 p-5 bg-white rounded shadow">
        <div class="flex flex-col gap-4 w-2/4">
          <Inputbox
            id="oldPassword"
            label="Password Lama"
            type="password"
            placeholder="passwordlama1234"
            bind:value={oldPassword}
            required
          />
          <Inputbox
            id="newPassword"
            label="Password Baru"
            type="password"
            placeholder="passwordbaru1234"
            bind:value={newPassword}
            required
          />
          <Inputbox
            id="newPasswordConfirm"
            label="Konfirmasi Password Baru"
            type="password"
            placeholder="passwordbaru1234"
            bind:value={newPasswordConfirm}
            required
          />
          <button class="w-fit text-sm py-2 px-5 bg-sky-700 text-white hover:bg-sky-600 rounded">
            Ganti Password
          </button>
        </div>
      </div>
    {/if}
  </div>
</div>