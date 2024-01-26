<script>
  import Icon from 'svelte-icons-pack';
  import FaUserCircle from 'svelte-icons-pack/fa/FaUserCircle';
  import AiOutlineSetting from 'svelte-icons-pack/ai/AiOutlineSetting';
  import RiSystemLockPasswordLine from 'svelte-icons-pack/ri/RiSystemLockPasswordLine';
  import RiSystemLogoutBoxRLine from 'svelte-icons-pack/ri/RiSystemLogoutBoxRLine';
  import RiSystemLoader4Fill from 'svelte-icons-pack/ri/RiSystemLoader4Fill';
  import RiDesignBallPenLine from 'svelte-icons-pack/ri/RiDesignBallPenLine';
  import HiSolidArrowLeft from 'svelte-icons-pack/hi/HiSolidArrowLeft';
  import Inputbox from './components/inputbox.svelte';
  import Growl from './components/growl.svelte';
  import axios from 'axios';

  export let title = '';
  export let user = {};
  const userOld = user;

  let growl, isAjaxSubmiited = false;

  const kelamin = [
    {label: 'Laki Laki', value: 'L'},
    {label: 'Perempuan', value: 'P'}
  ];

  const MODE_PROFILE = `profile`, MODE_SETTINGS = `settings`, MODE_PASSWORD = `password`;
  const MODE_PROFILE_EDIT = `profile_edit`;
  let MODE = MODE_PROFILE;

  const MENU = [
    {
      mode: MODE_PROFILE,
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

  async function submitEditProfile() {
    if (!user.nama || !user.alamat || !user.telepon || !user.jenis_kelamin) return growl.showWarning('Input tidak boleh kosong');
    // if (user.nama == userOld.nama || user.alamat == userOld.alamat
    //   || user.telepon == userOld.telepon || user.jenis_kelamin == userOld.jenis_kelamin
    // ) return growl.showWarning('Tidak ada perubahan !!');
    isAjaxSubmiited = true;
    await axios({
      method: 'post',
      url: '/api/edit-profile',
      data: {
        nama: user.nama,
        alamat: user.alamat,
        telepon: user.telepon,
        jenis_kelamin: user.jenis_kelamin
      },
      headers: { 'Content-Type': 'application/json' },
    }).then((res) => {
      isAjaxSubmiited = false;
      console.log(res.data);
      growl.showSuccess(res.data.message);
    }).catch((err) => {
      isAjaxSubmiited = false;
      growl.showError(err.response.data.message)
      console.log(err.response);
    });
  }

  let oldPassword = '', newPassword = '', newPasswordConfirm = '';
</script>

<svelte:head>
  <title>{title} | Bacaku</title>
</svelte:head>

<Growl bind:this={growl} />

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
          {#if MODE === m.mode || (m.mode === MODE_PROFILE && MODE === MODE_PROFILE_EDIT)}
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
    {#if MODE === MODE_PROFILE}
      <div class="flex flex-col gap-4 p-5 bg-white rounded shadow">
        <header class="flex flex-row justify-between items-center">
          <h1 class="text-2xl font-bold">Profil Saya</h1>
          <button on:click={() => MODE = MODE_PROFILE_EDIT} title="Edit profil" class="w-fit p-2 hover:bg-zinc-100 active:bg-zinc-200 rounded-full flex h-fit items-center justify-center">
            <Icon size="20" src={RiDesignBallPenLine} className="fill-orange-600" />
          </button>
        </header>
        <div class="flex flex-col gap-1">
          <span class="text-xs text-orange-600">Nama</span>
          <p>{user.nama}</p>
        </div>
        <div class="flex flex-col gap-1">
          <span class="text-xs text-orange-600">Alamat</span>
          <p>{user.alamat}</p>
        </div>
        <div class="flex flex-col gap-1">
          <span class="text-xs text-orange-600">Email</span>
          <p>{user.email}</p>
        </div>
        <div class="flex flex-col gap-1">
          <span class="text-xs text-orange-600">No. Telepon</span>
          <p>{user.telepon}</p>
        </div>
        <div class="flex flex-col gap-1">
          <span class="text-xs text-orange-600">Jenis Kelamin</span>
          <p>{user.jenis_kelamin === 'L' ? 'Laki - Laki' : 'Perempuan'}</p>
        </div>
      </div>
    {/if}
    {#if MODE === MODE_PROFILE_EDIT}
    <div class="flex flex-col gap-4 p-5 bg-white rounded shadow">
      <header class="flex flex-row gap-4 items-center">
        <button on:click={() => MODE = MODE_PROFILE} class="flex -mt-1 justify-center items-center hover:bg-zinc-100 active:bg-zinc-200 p-1.5 rounded-full">
          <Icon size="20" src={HiSolidArrowLeft} className="fill-sky-600"/>
        </button>
        <h1 class="text-2xl font-bold">Edit Profil</h1>
      </header>
      <div class="flex flex-col gap-4 w-2/4">
        <Inputbox
          id="nama"
          label="Nama"
          type="text"
          placeholder="Nama Lengkap"
          bind:value={user.nama}
        />
        <Inputbox
          id="alamat"
          label="Alamat"
          type="text"
          placeholder="Alamat"
          bind:value={user.alamat}
        />
        <Inputbox
          id="telepon"
          label="No. Telepon"
          type="text"
          placeholder="+628xxxxxxx"
          bind:value={user.telepon}
        />
        <Inputbox
          id="jenis_kelamin"
          label="Jenis Kelamin"
          type="radio"
          bind:value={user.jenis_kelamin}
          radios={kelamin}
        />
        <div class="flex flex-row items-center gap-2">
          <button
            disabled={isAjaxSubmiited}
            on:click={submitEditProfile}
            class="w-fit text-sm py-2 px-5 bg-sky-700 text-white hover:bg-sky-600 disabled:bg-sky-600 rounded"
          >
            Submit
          </button>
          {#if isAjaxSubmiited}
            <Icon size="16" src={RiSystemLoader4Fill} className="fill-zinc-800 -mt-1 animate-spin" />
          {/if}
        </div>
      </div>
    </div>
    {/if}
    {#if MODE === MODE_SETTINGS}
      <div class="flex flex-col gap-4 p-5 bg-white rounded shadow">
        <header class="flex flex-row justify-between items-center">
          <h1 class="text-2xl font-bold">Pengaturan</h1>
        </header>
      </div>
    {/if}
    {#if MODE === MODE_PASSWORD}
      <div class="flex flex-col gap-4 p-5 bg-white rounded shadow">
        <header class="flex flex-row justify-between items-center">
          <h1 class="text-2xl font-bold">Ganti Password</h1>
        </header>
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
            Submit
          </button>
        </div>
      </div>
    {/if}
  </div>
</div>