<script>
  export let book = {};
</script>

<div>
  {#if Object.keys(book).length === 0}
    <div>book empty</div>
  {/if}

  {#if Object.keys(book).length !== 0}
    <div>{book.judul}</div>
  {/if}
</div>