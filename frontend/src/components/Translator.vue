<script setup lang="ts">
  import { ref } from 'vue';
  import { useDebounceFn } from '@vueuse/core';

  import {Button} from "@/components/ui/button";
  import {Textarea} from "@/components/ui/textarea";
  import {Clipboard, MoveDown, MoveRight, Check} from "lucide-vue-next";
  import {Skeleton} from "@/components/ui/skeleton";

  const input = ref("");
  const loading = ref(false);
  const translation = ref("");

  const debounce = useDebounceFn(() => {
    if (input.value == "") {
      loading.value = false;
      translation.value = "";
      return
    }

    setTimeout(() => {
      loading.value = false;
      translation.value = input.value
    }, 1000)
  }, 700);

  const onChange = (event: { target: HTMLTextAreaElement }) => {
    input.value = event.target.value;
    loading.value = true;
    debounce()
  }

  const clipboardClicked = ref(false);

  const onCopy = () => {
    clipboardClicked.value = true;
    navigator.clipboard.writeText(translation.value)
    setTimeout(() => {
      clipboardClicked.value = false;
    }, 1500)
  }
</script>

<template>
  <div class="w-full h-96 max-h-4/5 grid grid-rows-[1fr_3rem_1fr] md:grid-rows-1 md:grid-cols-[1fr_3rem_1fr] gap-4">
    <div class="flex flex-col gap-4">
        <span
            class="flex justify-center items-center text-muted-foreground bg-muted/30 rounded-[calc(var(--radius)-2px)] px-2 py-1.5">
          Qualquer Lingua
        </span>
      <Textarea @input="onChange" class="h-full resize-none" placeholder="Digite em qualquer lingua para iniciar a tradução."/>
    </div>

    <div class="flex justify-center py-1.5">
      <MoveRight class="hidden md:block size-6 text-muted"/>
      <MoveDown class="md:hidden size-6 text-muted"/>
    </div>

    <div class="flex flex-col gap-4">
        <span
            class="flex justify-center items-center text-muted-foreground bg-muted/30 rounded-[calc(var(--radius)-2px)] px-2 py-1.5">
          Português
        </span>

      <div class="h-full p-4 border relative rounded-[calc(var(--radius)-2px)]">
        <div v-if="loading" class="w-full space-y-2">
          <Skeleton class="h-4 w-full" />
          <Skeleton class="h-4 w-10/12" />
        </div>
        <span v-else v-text="translation" />
        <Button @click="onCopy" variant="outline" size="icon" class="absolute bottom-4 right-4">
          <Transition mode="out-in" name="slide-up">
            <Clipboard v-if="!clipboardClicked" class="size-4" />
            <Check v-else class="size-4" />
          </Transition>
        </Button>
      </div>
    </div>
  </div>
</template>

<style scoped>
  .slide-up-enter-active,
  .slide-up-leave-active {
    transition: all 0.1s ease-out;
  }

  .slide-up-enter-from {
    opacity: 0;
    transform: translateY(15px);
  }

  .slide-up-leave-to {
    opacity: 0;
    transform: translateY(-15px);
  }
</style>