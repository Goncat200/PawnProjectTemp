<template>
  <div class="relative max-w-7xl mx-auto w-full px-4 py-6 rounded-2xl bg-gradient-to-br from-[#1e1e1e] to-[#0d0d0d] shadow-lg overflow-hidden">
    <div class="flex items-center justify-between mb-4">
      <h2 class="text-2xl font-extrabold text-[#f8f8f8]">Featured</h2>
      <div class="flex gap-2">
        <button @click="prev" class="carousel-arrow" aria-label="Prev">
          ‹
        </button>
        <button @click="next" class="carousel-arrow" aria-label="Next">
          ›
        </button>
      </div>
    </div>

    <div class="overflow-x-auto">
      <div class="flex gap-6 py-2 min-w-full">
        <div v-for="(row, rIdx) in rows" :key="rIdx" class="grid grid-cols-3 gap-6 min-w-[720px]">
          <div
            v-for="(item, cIdx) in row"
            :key="item.id"
            class="group relative rounded-xl overflow-hidden transition-all duration-400 border-2"
            :class="[(cIdx % 2 === 0) ? 'bg-[#202020] border-[#2c2c2c]' : 'bg-[#2a2a2a] border-[#1e1e1e]','hover:shadow-lg hover:-translate-y-2 hover:border-[#d4af37]']"
          >
            <img :src="item.image" alt="" class="w-full h-36 object-cover bg-[#1e1e1e]" />
            <div class="p-3 flex flex-col gap-1">
              <h3 class="text-md font-extrabold text-[#f8f8f8] truncate">{{ item.title }}</h3>
              <p class="text-sm text-gray-400 truncate">{{ item.description }}</p>
              <div class="flex items-center justify-between mt-2">
                <span class="text-lg font-bold text-[#d4af37]">${{ item.price }}</span>
                <button @click="viewItem(item)"
                        class="opacity-0 group-hover:opacity-100 transition px-3 py-1 rounded-full bg-[#c0c0c0] text-[#1e1e1e] font-bold hover:bg-[#d4af37]">
                  View
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'

const featured = ref([])
const index = ref(0)
const perSlide = 9

onMounted(async () => {
  try {
    const { data } = await axios.get('/featured')
    featured.value = Array.isArray(data) ? data : []
  } catch (err) {
    console.error('Failed to load featured', err)
  }
})

const slides = computed(() => {
  const arr = []
  for (let i = 0; i < featured.value.length; i += perSlide) {
    arr.push(featured.value.slice(i, i + perSlide))
  }
  return arr
})

// present each slide as 3 rows of 3 items
const rows = computed(() => {
  const items = slides.value[index.value] || []
  const result = []
  for (let r = 0; r < 3; r++) result.push(items.slice(r * 3, r * 3 + 3))
  return result
})

function prev() {
  if (index.value > 0) index.value--
}
function next() {
  if (index.value < slides.value.length - 1) index.value++
}
function viewItem(item) {
  alert(`View: ${item.title}`)
}
</script>

<style scoped>
.carousel-arrow {
  @apply w-9 h-9 flex items-center justify-center rounded-full bg-[#1e1e1e] border-2 border-[#d4af37] text-[#d4af37] font-bold transition;
}
.carousel-arrow:hover { @apply bg-[#d4af37] text-black; }
</style>