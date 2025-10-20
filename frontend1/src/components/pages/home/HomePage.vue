<template>
  <div class="min-h-screen bg-gradient-to-br from-[#1e1e1e] to-[#0d0d0d] flex flex-col gap-12 py-8">
    <HeroCarousel />
    <section class="max-w-7xl mx-auto w-full px-4">
      <h2 class="text-3xl font-extrabold text-[#f8f8f8] mb-6 tracking-wide">Marketplace</h2>
      <ProductGrid />
    </section>
  </div>
</template>

<script setup>
import HeroCarousel from '@/components/pages/home/HeroCarousel.vue'
import ProductGrid from '@/components/pages/home/OurProducts.vue'
</script>