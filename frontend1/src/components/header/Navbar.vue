<template>
  <nav class="flex items-center justify-between px-6 py-4 bg-[#0d0d0d] border-b border-[#2c2c2c]">
    <!-- Left: Logo -->
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 flex items-center justify-center bg-gradient-to-br from-[#1e1e1e] to-[#2c2c2c] rounded-md border-2 border-[#d4af37]">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" class="text-[#f8f8f8]">
          <path d="M12 2v6" stroke="#f8f8f8" stroke-width="1.6" stroke-linecap="round"/>
          <circle cx="12" cy="14" r="6" stroke="#f8f8f8" stroke-width="1.6"/>
        </svg>
      </div>
      <span class="text-lg font-extrabold text-[#f8f8f8]">PayPawn</span>
    </div>

    <!-- Center: Search -->
    <div class="flex-1 px-6">
      <form @submit.prevent="onSearch" class="max-w-2xl mx-auto relative">
        <input
          v-model="search"
          type="search"
          placeholder="Search digital goods..."
          class="w-full px-4 py-2 rounded-full bg-[#1e1e1e] text-[#f8f8f8] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-blue-500/50 transition duration-300"
          aria-label="Search products"
        />
        <button type="submit" class="absolute right-2 top-1/2 -translate-y-1/2 p-2 rounded-full bg-[#2c2c2c] hover:bg-[#d4af37] transition">
          🔍
        </button>
      </form>
    </div>

    <!-- Right: Icons -->
    <div class="flex items-center gap-3">
      <button class="icon-btn" title="Games">🎮</button>
      <button class="icon-btn" title="Marketplace">🛍️</button>
      <button class="icon-btn" title="Analytics">📈</button>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const search = ref('')
const router = useRouter()

async function onSearch() {
  const q = (search.value || '').trim()
  if (!q) return
  try {
    // backend expects POST /search with { q: string }
    const res = await axios.post('/search', { q })
    // navigate to home with query and cache results in sessionStorage for a quick view
    sessionStorage.setItem('searchResults', JSON.stringify(res.data || []))
    await router.push({ path: '/', query: { q } })
  } catch (err) {
    console.error('Search failed', err)
    alert('Search failed, check console.')
  }
}
</script>

<style scoped>
.icon-btn {
  @apply w-10 h-10 flex items-center justify-center rounded-full bg-[#1e1e1e] text-[#f8f8f8] shadow transition duration-300 border-2 border-transparent;
}
.icon-btn:hover, .icon-btn:focus {
  @apply border-[#d4af37] shadow-[0_0_12px_2px_#d4af37cc] outline-none;
}
</style>