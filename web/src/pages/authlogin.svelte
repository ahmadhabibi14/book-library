<script>
  import Inputbox from "./components/inputbox.svelte";
  import axios from 'axios';

  export let title = '';

  let email = '', password = '', isLoginSubmitted = false;
  async function Login() {
    isLoginSubmitted = true;
    if (email == '' || password == '') return alert('Please fill all fields');

    await axios.post('/api/login', { email, password }).then((res) => {
      console.log(res.data)
      alert(res.data.message);
      setTimeout(() => {
        window.location.href = '/';
      }, 1200);
    }).catch((err) => {
      alert(err.response.data.message)
    })
  }
</script>

<div class="w-full max-h-screen h-screen bg-zinc-100 text-zinc-800">
  <main class="flex flex-row justify-center items-center gap-16 w-full h-fit mx-auto pt-20">
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
        <button on:click={Login} class="w-full rounded-md py-2 px-11 text-white bg-sky-800 hover:bg-sky-700 cursor-pointer">
          Login
        </button>
        <span class="text-sm text-center">Belum punya akun? <a href="/register" class="text-sky-700 hover:text-sky-500">Register</a></span>
      </div>
    </div>
  </main>
</div>