import { resolve } from 'path';
import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    svelte()
  ],
  root: resolve('./web/src'),
  base: '/static/',
  server: {
    host: 'localhost',
    port: 3000,
    open: false,
    watch: {
      usePolling: true,
      disableGlobbing: false,
    },
  },
  resolve: {
    extensions: ['.js', '.jsx', '.json', '.svelte'],
  },
  build: {
    outDir: resolve('./web/dist'),
    assetsDir: '',
    manifest: 'manifest.json',
    emptyOutDir: true,
    target: 'es2015',
    rollupOptions: {
      input: {
        main: resolve('./web/src/js/main.js'),
      },
      output: {
        chunkFileNames: undefined,
      },
    },
  },
})
