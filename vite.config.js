import path from 'path';
import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    svelte()
  ],
  root: path.resolve('./static'),
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./static"),
    },
    extensions: ['.js', '.jsx', '.json', '.svelte'],
  },
  base: '/static/',
  publicDir: false,
  build: {
    manifest: true,
    target: 'es2015',
    emptyOutDir: true,
    outDir: path.resolve('./static/dist'),
    rollupOptions: {
      input: {
        main: path.resolve('./static/js/main.js'),
      },
      output: {
        chunkFileNames: undefined,
      },
      external: [
        "svelte",
        "@babel/plugin-syntax-dynamic-import",
        "@inertiajs/inertia",
        "@inertiajs/inertia-svelte",
        "@inertiajs/progress",
        "@sveltejs/vite-plugin-svelte"
      ]
    },
    assetsInlineLimit: 0
  },
})