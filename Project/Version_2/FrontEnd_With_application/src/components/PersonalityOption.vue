<!-- <script setup lang="ts">
defineProps<{
  name: string;
  image: string;
  description: string;
  selected: boolean;
}>();
</script>

<template>
  <div
    class="relative p-4 border rounded-lg transition-all cursor-pointer hover:shadow-md group"
    :class="selected ? 'border-primary-500 bg-primary-50' : 'border-gray-200'"
  >
    <img :src="image" :alt="name" class="w-16 h-16 rounded-full mx-auto mb-2 object-cover" />
    <p class="text-center font-medium">{{ name }}</p>
    <div
      class="hidden group-hover:block absolute bottom-full left-1/2 transform -translate-x-1/2 w-48 p-2 mb-2 bg-white rounded-lg shadow-lg border border-gray-200 z-10"
    >
      <p class="text-sm text-gray-700">{{ description }}</p>
    </div>
    <div
      v-if="selected"
      class="absolute -top-2 -right-2 w-6 h-6 bg-primary-500 rounded-full flex items-center justify-center"
    >
      <svg
        class="w-4 h-4 text-white"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M5 13l4 4L19 7"
        />
      </svg>
    </div>
  </div>
</template> -->

<script setup lang="ts">
defineProps<{
  name: string;
  image: string;
  description: string;
  selected: boolean;
}>();
</script>

<template>
  <div
    class="relative p-4 border rounded-lg transition-all cursor-pointer hover:shadow-md group"
    :class="selected ? 'border-primary-500 bg-primary-50' : 'border-gray-200'"
  >
    <img :src="image" :alt="name" class="w-16 h-16 rounded-full mx-auto mb-2 object-cover" />
    <p class="text-center font-medium">{{ name }}</p>
    <div
      class="hidden group-hover:block absolute bottom-full left-1/2 transform -translate-x-1/2 w-48 p-2 mb-2 bg-white rounded-lg shadow-lg border border-gray-200 z-10"
    >
      <p class="text-sm text-gray-700">{{ description }}</p>
    </div>
    <div
      v-if="selected"
      class="absolute -top-2 -right-2 w-6 h-6 bg-primary-500 rounded-full flex items-center justify-center"
    >
      <svg
        class="w-4 h-4 text-white"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M5 13l4 4L19 7"
        />
      </svg>
    </div>
  </div>
</template>