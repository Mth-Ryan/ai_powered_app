<script setup lang="ts">
import Header from "@/components/Header.vue";
import Translator from "@/components/Translator.vue";
</script>

<template>
  <Header/>
  <div class="container py-8 flex flex-col gap-24 justify-center items-center h-[calc(100vh-4rem)]">
    <div class="text-center space-y-4">
      <span class="rounded-full bg-muted/60 text-muted-foreground py-1 px-4">
        🦾 baseado no modelo GPT-3.5
      </span>
      <h1 class="font-bold text-6xl">AI Translator</h1>
      <p class="text-muted-foreground max-w-96">
        Traduza qualquer lingua para português com ajuda
        de inteligência artificial.
      </p>
    </div>
    <Translator />
  </div>
</template>

<style scoped>
</style>
