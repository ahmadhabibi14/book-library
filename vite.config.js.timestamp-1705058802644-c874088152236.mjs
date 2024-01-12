// vite.config.js
import { resolve } from "path";
import { defineConfig } from "file:///home/habi/Dev/githubRepos/book-library/node_modules/.pnpm/vite@5.0.10/node_modules/vite/dist/node/index.js";
import { svelte } from "file:///home/habi/Dev/githubRepos/book-library/node_modules/.pnpm/@sveltejs+vite-plugin-svelte@3.0.1_svelte@4.2.8_vite@5.0.10/node_modules/@sveltejs/vite-plugin-svelte/src/index.js";
var vite_config_default = defineConfig({
  plugins: [
    svelte()
  ],
  root: resolve("./web/src"),
  base: "/static/",
  server: {
    host: "localhost",
    port: 3e3,
    open: false,
    watch: {
      usePolling: true,
      disableGlobbing: false
    }
  },
  resolve: {
    extensions: [".js", ".jsx", ".json", ".svelte"]
  },
  build: {
    outDir: resolve("./web/dist"),
    assetsDir: "",
    manifest: true,
    emptyOutDir: true,
    target: "es2015",
    rollupOptions: {
      input: {
        main: resolve("./web/src/js/main.js")
      },
      output: {
        chunkFileNames: void 0
      }
    }
  }
});
export {
  vite_config_default as default
};
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsidml0ZS5jb25maWcuanMiXSwKICAic291cmNlc0NvbnRlbnQiOiBbImNvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9kaXJuYW1lID0gXCIvaG9tZS9oYWJpL0Rldi9naXRodWJSZXBvcy9ib29rLWxpYnJhcnlcIjtjb25zdCBfX3ZpdGVfaW5qZWN0ZWRfb3JpZ2luYWxfZmlsZW5hbWUgPSBcIi9ob21lL2hhYmkvRGV2L2dpdGh1YlJlcG9zL2Jvb2stbGlicmFyeS92aXRlLmNvbmZpZy5qc1wiO2NvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9pbXBvcnRfbWV0YV91cmwgPSBcImZpbGU6Ly8vaG9tZS9oYWJpL0Rldi9naXRodWJSZXBvcy9ib29rLWxpYnJhcnkvdml0ZS5jb25maWcuanNcIjtpbXBvcnQgeyByZXNvbHZlIH0gZnJvbSAncGF0aCc7XG5pbXBvcnQgeyBkZWZpbmVDb25maWcgfSBmcm9tICd2aXRlJ1xuaW1wb3J0IHsgc3ZlbHRlIH0gZnJvbSAnQHN2ZWx0ZWpzL3ZpdGUtcGx1Z2luLXN2ZWx0ZSdcblxuLy8gaHR0cHM6Ly92aXRlanMuZGV2L2NvbmZpZy9cbmV4cG9ydCBkZWZhdWx0IGRlZmluZUNvbmZpZyh7XG4gIHBsdWdpbnM6IFtcbiAgICBzdmVsdGUoKVxuICBdLFxuICByb290OiByZXNvbHZlKCcuL3dlYi9zcmMnKSxcbiAgYmFzZTogJy9zdGF0aWMvJyxcbiAgc2VydmVyOiB7XG4gICAgaG9zdDogJ2xvY2FsaG9zdCcsXG4gICAgcG9ydDogMzAwMCxcbiAgICBvcGVuOiBmYWxzZSxcbiAgICB3YXRjaDoge1xuICAgICAgdXNlUG9sbGluZzogdHJ1ZSxcbiAgICAgIGRpc2FibGVHbG9iYmluZzogZmFsc2UsXG4gICAgfSxcbiAgfSxcbiAgcmVzb2x2ZToge1xuICAgIGV4dGVuc2lvbnM6IFsnLmpzJywgJy5qc3gnLCAnLmpzb24nLCAnLnN2ZWx0ZSddLFxuICB9LFxuICBidWlsZDoge1xuICAgIG91dERpcjogcmVzb2x2ZSgnLi93ZWIvZGlzdCcpLFxuICAgIGFzc2V0c0RpcjogJycsXG4gICAgbWFuaWZlc3Q6IHRydWUsXG4gICAgZW1wdHlPdXREaXI6IHRydWUsXG4gICAgdGFyZ2V0OiAnZXMyMDE1JyxcbiAgICByb2xsdXBPcHRpb25zOiB7XG4gICAgICBpbnB1dDoge1xuICAgICAgICBtYWluOiByZXNvbHZlKCcuL3dlYi9zcmMvanMvbWFpbi5qcycpLFxuICAgICAgfSxcbiAgICAgIG91dHB1dDoge1xuICAgICAgICBjaHVua0ZpbGVOYW1lczogdW5kZWZpbmVkLFxuICAgICAgfSxcbiAgICB9LFxuICB9LFxufSlcbiJdLAogICJtYXBwaW5ncyI6ICI7QUFBdVMsU0FBUyxlQUFlO0FBQy9ULFNBQVMsb0JBQW9CO0FBQzdCLFNBQVMsY0FBYztBQUd2QixJQUFPLHNCQUFRLGFBQWE7QUFBQSxFQUMxQixTQUFTO0FBQUEsSUFDUCxPQUFPO0FBQUEsRUFDVDtBQUFBLEVBQ0EsTUFBTSxRQUFRLFdBQVc7QUFBQSxFQUN6QixNQUFNO0FBQUEsRUFDTixRQUFRO0FBQUEsSUFDTixNQUFNO0FBQUEsSUFDTixNQUFNO0FBQUEsSUFDTixNQUFNO0FBQUEsSUFDTixPQUFPO0FBQUEsTUFDTCxZQUFZO0FBQUEsTUFDWixpQkFBaUI7QUFBQSxJQUNuQjtBQUFBLEVBQ0Y7QUFBQSxFQUNBLFNBQVM7QUFBQSxJQUNQLFlBQVksQ0FBQyxPQUFPLFFBQVEsU0FBUyxTQUFTO0FBQUEsRUFDaEQ7QUFBQSxFQUNBLE9BQU87QUFBQSxJQUNMLFFBQVEsUUFBUSxZQUFZO0FBQUEsSUFDNUIsV0FBVztBQUFBLElBQ1gsVUFBVTtBQUFBLElBQ1YsYUFBYTtBQUFBLElBQ2IsUUFBUTtBQUFBLElBQ1IsZUFBZTtBQUFBLE1BQ2IsT0FBTztBQUFBLFFBQ0wsTUFBTSxRQUFRLHNCQUFzQjtBQUFBLE1BQ3RDO0FBQUEsTUFDQSxRQUFRO0FBQUEsUUFDTixnQkFBZ0I7QUFBQSxNQUNsQjtBQUFBLElBQ0Y7QUFBQSxFQUNGO0FBQ0YsQ0FBQzsiLAogICJuYW1lcyI6IFtdCn0K
