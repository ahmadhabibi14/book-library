<script>
  import Icon from "svelte-icons-pack";
  import FiLoader from "svelte-icons-pack/fi/FiLoader";
  import Inputbox from "./components/inputbox.svelte";
  import Growl from "./components/growl.svelte";
  import axios from 'axios';
  import { onMount } from "svelte";

  export let title = '';
  const kelamin = [
    {label: 'Laki Laki', value: 'L'},
    {label: 'Perempuan', value: 'P'}
  ];
  let growl;

  let email = '', password = '', nama = '', jenis_kelamin = 'L', alamat = '', telepon = '';
  let isSubmitted = false;
  async function Register() {
    isSubmitted = true;
    if (email == '' || password == '' || nama == '' || jenis_kelamin == '' || alamat == '' || telepon == '') return growl.showWarning('Please fill all fields');

    await axios.post(
      '/api/register',
      { email, password, nama, jenis_kelamin, alamat, telepon}
    ).then((res) => {
      isSubmitted = false;
      growl.showSuccess(res.data.message);
      setTimeout(() => {
        window.location.href = '/';
      }, 1200);
    }).catch((err) => {
      console.log(err.response.data);
      isSubmitted = false;
      growl.showError(JSON.stringify(err.response.data.errors));
    })
  }

  onMount(() => {
    console.log('Kelamin', kelamin)
  })
</script>

<svelte:head>
  <title>Register | ePerpus</title>
</svelte:head>

<Growl bind:this={growl} />
<div class="w-full min-h-screen bg-zinc-100 text-zinc-800">
  <main class="flex flex-row justify-between w-[70%] h-fit mx-auto py-20">
    <div class="w-[400px] mt-8">
      <img src="static/img/woman-book.png" alt="" />
    </div>
    <div class="w-[450px] bg-white shadow-lg flex flex-col gap-4 p-5 rounded-md">
      <header class="w-full">
        <h1 class="text-center font-bold text-3xl decoration-sky-800 underline">{title}</h1>
      </header>
      <div class="flex flex-col gap-4">
        <Inputbox
          id="nama"
          label="Nama"
          type="text"
          placeholder="Namamu ..."
          bind:value={nama}
          required
        />
        <Inputbox
          id="email"
          label="Email"
          type="email"
          placeholder="nama@email.com"
          bind:value={email}
          required
        />
        <Inputbox
          id="alamat"
          label="Alamat"
          type="text"
          placeholder="Jln. Raya Sintung...."
          bind:value={alamat}
          required
        />
        <Inputbox
          id="telepon"
          label="No. Telepon"
          type="tel"
          placeholder="+6283xxxxxxxx"
          bind:value={telepon}
          required
        />
        <Inputbox
          id="jenis_kelamin"
          label="Jenis Kelamin"
          type="radio"
          bind:value={jenis_kelamin}
          radios={kelamin}
          required
        />
        <Inputbox
          id="password"
          label="Password"
          type="password"
          placeholder="password123"
          bind:value={password}
          required
        />
      </div>
      <div class="flex flex-col gap-5 mt-3">
        <button
          on:click={Register}
          disabled={isSubmitted}
          class="w-full rounded-md py-2 px-11 text-white bg-sky-800 hover:bg-sky-700
            cursor-pointer flex justify-center items-center disabled:bg-sky-600"
        >
          {#if isSubmitted}
            <Icon className="animate-spin fill-white" size="24" src={FiLoader}/>
          {/if}
          {#if !isSubmitted}
            <span>Register</span>
          {/if}
        </button>
        <span class="text-sm text-center">Sudah punya akun? <a href="/login" class="text-sky-700 hover:text-sky-500">Login</a></span>
      </div>
    </div>
  </main>
</div>