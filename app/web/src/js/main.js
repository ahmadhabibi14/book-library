// @ts-nocheck
import { createInertiaApp } from '@inertiajs/inertia-svelte'
import { InertiaProgress } from '@inertiajs/progress'
import Layout from '../pages/_layout.svelte'
import '../css/main.css'

InertiaProgress.init();

createInertiaApp({
  resolve: async (name) => {
    const comps = import.meta.glob('../pages/**/*.svelte');
    const match = comps[`../pages/${name}.svelte`];
    const page = (await match());

    if (name.startsWith('auth') || name.startsWith('_')) return Object.assign({layout: undefined}, page);
    else return Object.assign({layout: Layout}, page);
  },
  setup({ el, App, props }) {
    new App({ target: el, props })
  },
  progress: {
    delay: 250,
    color: '#0369a1',
    includeCSS: true,
    showSpinner: false,
  },
});
