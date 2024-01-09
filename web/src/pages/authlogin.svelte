<script>
  import Icon from "svelte-icons-pack";
  import FiLoader from "svelte-icons-pack/fi/FiLoader";
  import Inputbox from "./components/inputbox.svelte";
  import Growl from "./components/growl.svelte";
  import axios from 'axios';

  export let title = '';
  let growl;

  let email = '', password = '', isSubmitted = false;
  async function Login() {
    isSubmitted = true;
    if (email == '' || password == '') return growl.showWarning('Please fill all fields');

    await axios.post('/api/login', { email, password }).then((res) => {
      isSubmitted = false;
      growl.showSuccess(res.data.message);
      setTimeout(() => {
        window.location.href = '/';
      }, 1200);
    }).catch((err) => {
      isSubmitted = false;
      growl.showError(err.response.data.message)
    })
  }
</script>

<svelte:head>
  <title>Login | ePerpus</title>
</svelte:head>

<Growl bind:this={growl} />

<div class="w-full min-h-screen bg-zinc-100 text-zinc-800">
  <main class="flex flex-row justify-between w-[70%] items-center h-fit mx-auto py-20">
    <div class="w-[400px]">
      <img src="static/img/woman-book.png" alt="" />
    </div>
    <div class="w-[450px] bg-white shadow-lg flex flex-col gap-4 p-5 rounded-md">
      <header class="w-full">
        <h1 class="text-center font-bold text-3xl decoration-sky-800 underline">{title}</h1>
      </header>
      <div class="flex flex-col gap-4">
        <Inputbox
          id="email"
          label="Email"
          type="email"
          placeholder="nama@email.com"
          bind:value={email}
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
          on:click={Login}
          disabled={isSubmitted}
          class="w-full rounded-md py-2 px-11 text-white bg-sky-800 hover:bg-sky-700
            cursor-pointer flex justify-center items-center disabled:bg-sky-600"
        >
          {#if isSubmitted}
            <Icon className="animate-spin fill-white" size="24" src={FiLoader}/>
          {/if}
          {#if !isSubmitted}
            <span>Login</span>
          {/if}
        </button>
        <span class="text-sm text-center">Belum punya akun? <a href="/register" class="text-sky-700 hover:text-sky-500">Register</a></span>
      </div>
    </div>
  </main>
</div>