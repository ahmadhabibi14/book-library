<script>
  import { onMount } from 'svelte';
  import Icon from 'svelte-icons-pack/Icon.svelte';
  import AiOutlineEye from 'svelte-icons-pack/ai/AiOutlineEye';
  import AiOutlineEyeInvisible from 'svelte-icons-pack/ai/AiOutlineEyeInvisible';

  export let id;
  export let value;
  export let label;
  export let type = 'text';
  export let placeholder = '';
  export let required = false;
  let isShowPassword = false;
  let inputElm;
  
  onMount(() => inputElm.type = type)
  function toggleShowPassword() {
    isShowPassword = !isShowPassword;
    if (isShowPassword) inputElm.type = 'text';
    else inputElm.type = 'password';
  }
</script>

<div class={`flex flex-col gap-2 ${type === 'password' ? 'relative' : ''}`} >
  <label for={id} class="text-sm text-zinc-600 ml-2">
    <span>{label}</span>
    {#if required}
      <span class="text-red-500"> *</span>
    {/if}
  </label>
  <input
    class={`rounded-md w-full border border-zinc-300 py-2 caret-sky-800 focus:border-sky-800 focus:outline focus:outline-sky-800 ${type === 'password' ? 'pl-4 pr-10' : 'px-4'}`}
    bind:value={value} {id} bind:this={inputElm} {placeholder}/>
  {#if type === 'password'}
    <button class="absolute right-2 top-9" title="Show/Hide Password" on:click={toggleShowPassword}>
      {#if !isShowPassword}
        <Icon className="fill-zinc-700 hover:fill-sky-700" size="24" src={AiOutlineEye}/>
      {/if}
      {#if isShowPassword}
        <Icon className="fill-zinc-700 hover:fill-sky-700" size="24" src={AiOutlineEyeInvisible}/>
      {/if}
    </button>
  {/if}
</div>

