<template>
  <footer class="bg-[#0d0d0d] border-t-4 border-t-[#2c2c2c] pt-10 pb-4">
    <div class="max-w-7xl mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-8 mb-6">
      <!-- Left: Socials -->
      <div class="flex flex-col gap-4">
        <span class="text-lg font-bold text-[#f8f8f8] mb-2">Join us</span>
        <div class="flex gap-4">
          <a href="#" class="footer-icon" aria-label="Discord">Discord</a>
          <a href="#" class="footer-icon" aria-label="Telegram">Telegram</a>
          <a href="#" class="footer-icon" aria-label="X">X</a>
          <a href="#" class="footer-icon" aria-label="YouTube">YouTube</a>
        </div>
      </div>
      <!-- Center: Newsletter -->
      <div class="flex flex-col gap-4 items-center">
        <span class="text-lg font-bold text-[#f8f8f8] mb-2">Newsletter</span>
        <form @submit.prevent="subscribe" class="flex gap-2 w-full max-w-xs">
          <input
            v-model="email"
            type="email"
            placeholder="Your email"
            class="flex-1 px-4 py-2 rounded-l-full bg-[#1e1e1e] text-[#f8f8f8] placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-[#d4af37]"
            required
          />
          <button
            type="submit"
            class="px-5 py-2 rounded-r-full bg-[#d4af37] text-[#0d0d0d] font-bold"
          >
            Join
          </button>
        </form>
        <span v-if="subscribed" class="text-[#d4af37] text-sm mt-1">Subscribed!</span>
      </div>
      <!-- Right: Support/Contact/Terms -->
      <div class="flex flex-col gap-2 items-end md:items-start">
        <span class="text-lg font-bold text-[#f8f8f8] mb-2">Support</span>
        <a href="#" class="footer-link">Contact</a>
        <a href="#" class="footer-link">Terms of Service</a>
        <a href="#" class="footer-link">Privacy Policy</a>
      </div>
    </div>
    <div class="border-t border-[#2c2c2c] pt-4 flex flex-col items-center">
      <div class="w-full h-3 bg-[repeating-linear-gradient(90deg,#1e1e1e_0_16px,#2c2c2c_16px_32px)] rounded-t"></div>
      <span class="text-[#c0c0c0] text-xs mt-2">&copy; 2025 PayPawn. All rights reserved.</span>
    </div>
  </footer>
</template>

<script setup>
import { ref } from 'vue'
const email = ref('')
const subscribed = ref(false)
function subscribe() {
  if (email.value) {
    subscribed.value = true
    setTimeout(() => (subscribed.value = false), 3000)
    email.value = ''
  }
}
</script>

<style scoped>
.footer-icon {
  @apply rounded-full bg-[#1e1e1e] p-2 shadow transition duration-300 border-2 border-transparent;
}
.footer-icon:hover, .footer-icon:focus {
  @apply border-[#d4af37] shadow-[0_0_12px_2px_#d4af37cc] outline-none;
}
.footer-link {
  @apply text-[#c0c0c0] hover:text-[#d4af37] transition font-light;
}
</style>