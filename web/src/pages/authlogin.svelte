<script>
  export let title = '';

  let email = '', password = ''
</script>

<div class="w-full max-h-screen h-screen bg-sky-800 text-zinc-800">
  <main class="flex flex-row justify-center items-center w-full h-fit mx-auto">
    <div class="mt-14 w-[450px] bg-white shadow-lg flex flex-col gap-4 p-5">
      <header class="w-full">
        <h1 class="text-center font-bold text-3xl decoration-sky-800 underline">{title}</h1>
      </header>
      <div class="flex flex-col gap-4">
        <div class="flex flex-col gap-2">
          <label
            for="email"
            class="text-sm text-zinc-600 ml-2"
          >Email <span class="text-red-500">*</span></label>
          <input
            type="email"
            name="email"
            id="email"
            placeholder="nama@email.com"
            class="w-full border border-zinc-300 py-3 px-4 caret-sky-800 focus:border-sky-800 focus:outline focus:outline-sky-800"
            bind:value={email}
          />
        </div>
        <div class="flex flex-col gap-2">
          <label
            for="password"
            class="text-sm text-zinc-600 ml-2"
          >Password <span class="text-red-500">*</span></label>
          <input
            type="password"
            name="password"
            id="password"
            placeholder="password123"
            class="w-full border border-zinc-300 py-3 px-4 caret-sky-800 focus:border-sky-800 focus:outline focus:outline-sky-800"
            bind:value={password}
          />
        </div>
      </div>
      <div class="flex flex-row-reverse">
        <button class="mt-4 py-2 px-11 text-white bg-sky-800 hover:bg-sky-700 cursor-pointer">
          Login
        </button>
      </div>
    </div>
  </main>
</div>