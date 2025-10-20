<template>
  <div
    class="relative group rounded-xl overflow-hidden transition-all duration-500 border-2"
    :class="[
      isEven ? 'bg-[#202020] border-[#2c2c2c]' : 'bg-[#2a2a2a] border-[#1e1e1e]',
      'hover:shadow-lg hover:-translate-y-2 hover:border-[#d4af37]'
    ]"
  >
    <img :src="product.image || '/logo.png'" alt="" class="w-full h-40 object-cover bg-[#1e1e1e]" />
    <div class="p-4 flex flex-col gap-2">
      <h3 class="text-lg font-extrabold text-[#f8f8f8] truncate">{{ product.title }}</h3>
      <p class="text-sm text-gray-400 font-light truncate">{{ product.description }}</p>
      <div class="flex items-center justify-between mt-2">
        <span class="text-lg font-bold text-[#d4af37]">${{ product.price }}</span>
        <button
          class="opacity-0 group-hover:opacity-100 transition-all duration-300 px-4 py-1 rounded-full bg-[#c0c0c0] text-[#1e1e1e] font-bold hover:bg-[#d4af37]"
          @click="onBuy"
        >
          Buy
        </button>
      </div>
    </div>
    <button
      class="absolute top-3 right-3 z-10 p-2 rounded-full bg-[#c0c0c0] text-blue-500 shadow-lg hover:scale-110 transition-all duration-300"
      @click.stop="onAdd"
      aria-label="Add"
    >
      +
    </button>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue'
const props = defineProps({
  product: { type: Object, required: true },
  isEven: { type: Boolean, default: false }
})
const emit = defineEmits(['add', 'buy'])

function onAdd() {
  emit('add', props.product)
}
function onBuy() {
  emit('buy', props.product)
}
</script>