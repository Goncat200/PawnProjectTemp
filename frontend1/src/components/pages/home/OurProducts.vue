<template>
  <div>
    <div v-if="loading" class="flex justify-center items-center py-20">
      <span class="text-[#c0c0c0] text-xl animate-pulse">Loading products…</span>
    </div>

    <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-6">
      <Card
        v-for="(product, idx) in products"
        :key="product.id"
        :product="product"
        :isEven="(idx + Math.floor(idx/5)) % 2 === 0"
        @add="addToCart"
        @buy="buyProduct"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import Card from '@/components/main-objects/Card.vue'

const products = ref([])
const loading = ref(true)

onMounted(async () => {
  loading.value = true
  try {
    const { data } = await axios.get('/products')
    products.value = Array.isArray(data) ? data : []
    // check for search results in sessionStorage (from Navbar)
    const searchResults = sessionStorage.getItem('searchResults')
    const params = new URLSearchParams(window.location.search)
    if (params.get('q') && searchResults) {
      products.value = JSON.parse(searchResults)
      sessionStorage.removeItem('searchResults')
    }
  } catch (err) {
    console.error('Load products failed', err)
  } finally {
    loading.value = false
  }
})

async function addToCart(product) {
  // simple frontend cart demo (localStorage)
  const cart = JSON.parse(localStorage.getItem('cart') || '[]')
  cart.push(product)
  localStorage.setItem('cart', JSON.stringify(cart))
  alert(`Added ${product.title} to cart`)
}

async function buyProduct(product) {
  try {
    const user = (await axios.get('/user')).data
    const res = await axios.post('/purchase', { product_id: product.id, user_id: user.id })
    if (res.status === 200 || res.data?.status === 'success') {
      alert(`Purchase successful: ${product.title}`)
    } else {
      alert('Purchase response: ' + JSON.stringify(res.data))
    }
  } catch (err) {
    console.error('Purchase failed', err)
    alert('Purchase failed, check console.')
  }
}
</script>