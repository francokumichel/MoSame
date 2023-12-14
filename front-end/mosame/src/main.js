import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import store from "./store";
import Toaster from "@meforma/vue-toaster";

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(store)
app.use(Toaster)
app.mount('#app')
