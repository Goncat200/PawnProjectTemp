<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import autoAnimate from '@formkit/auto-animate'

import Navbar from '@/components/header/Navbar.vue'
import Footer from '@/components/footer/Footer.vue'
import Profile from './components/pages/profile/ProfilePage.vue'
import Home from './components/pages/home/HomePage.vue'

const parent = ref(null)
const startpage = ref(true)
const apiStatus = ref('unknown')

function toggleStartPage() {
  startpage.value = !startpage.value
}

// set API base url for all axios calls
axios.defaults.baseURL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000'
axios.defaults.timeout = 5000

onMounted(async () => {
  if (parent.value) autoAnimate(parent.value)

  try {
    const res = await axios.get('/user')
    apiStatus.value = `OK - ${res.data.username}`
  } catch (err) {
    apiStatus.value = 'offline'
    console.error('API check failed', err)
  }
})
</script>

<template>
  <div
    ref="parent"
    class="min-h-screen flex flex-col bg-gradient-to-br from-[#1e1e1e] to-[#0d0d0d] font-rubik"
  >
    <Navbar />
    <main class="flex-1 flex flex-col p-6">
      <div class="max-w-7xl w-full mx-auto">
        <div class="flex items-center justify-between mb-6">
          <div>
            <h1 class="text-2xl font-extrabold text-[#f8f8f8]">PayPawn Marketplace</h1>
            <p class="text-sm text-gray-400">Connected backend: {{ apiStatus }}</p>
          </div>
          <div class="flex items-center gap-4">
            <button
              class="px-4 py-2 rounded-md bg-[#d4af37] text-black font-bold"
              @click="toggleStartPage"
            >
              Toggle View
            </button>
          </div>
        </div>

        <section>
          <Home v-if="startpage" />
          <Profile v-else />
        </section>
      </div>
    </main>
    <Footer />
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@900;300&display=swap');
.font-rubik { font-family: 'Rubik', 'Inter', 'IBM Plex Sans', sans-serif; }
</style>
