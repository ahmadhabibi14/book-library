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

    return Object.assign({layout: name.startsWith('auth') || name.startsWith('error') ? undefined : Layout}, page);
  },
  setup({ el, App, props }) {
    new App({ target: el, props })
  },
});
