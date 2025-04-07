<!-- <script setup lang="ts">
defineProps<{
  index: number;
  param: {
    key: string;
    value: string;
  };
}>();

const emit = defineEmits<{
  remove: [index: number];
  update: [index: number, key: string, value: string];
}>();
</script>

<template>
  <div class="flex gap-4 items-center">
    <input
      type="text"
      :value="param.key"
      @input="(e) => emit('update', index, (e.target as HTMLInputElement).value, param.value)"
      placeholder="Parameter name"
      class="flex-1 rounded-lg border-gray-300 focus:border-primary-500 focus:ring-primary-500"
    />
    <input
      type="text"
      :value="param.value"
      @input="(e) => emit('update', index, param.key, (e.target as HTMLInputElement).value)"
      placeholder="Value"
      class="flex-1 rounded-lg border-gray-300 focus:border-primary-500 focus:ring-primary-500"
    />
    <button
      @click="emit('remove', index)"
      class="text-red-500 hover:text-red-700"
      type="button"
    >
      <svg
        class="w-5 h-5"
        fill="none"
        stroke="currentColor"
        viewBox="0 0 24 24"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
        />
      </svg>
    </button>
  </div>
</template> -->


<script setup lang="ts">
const props = defineProps<{
  index: number;
  param: { key: string; value: string };
}>();

const emit = defineEmits<{
  (e: 'remove', index: number): void;
  (e: 'update', index: number, key: string, value: string): void;
}>();

const updateKey = (event: Event) => {
  const target = event.target as HTMLInputElement;
  emit('update', props.index, target.value, props.param.value);
};

const updateValue = (event: Event) => {
  const target = event.target as HTMLInputElement;
  emit('update', props.index, props.param.key, target.value);
};
</script>

<template>
  <div class="grid grid-cols-2 gap-4 items-center">
    <input
      type="text"
      :value="param.key"
      @input="updateKey"
      placeholder="Parameter name"
      class="w-full p-2 rounded-lg border bg-white/50 focus:border-primary-500 focus:ring-primary-500"
    />
    <div class="flex items-center gap-2">
      <input
        type="text"
        :value="param.value"
        @input="updateValue"
        placeholder="Value"
        class="w-full p-2 rounded-lg border bg-white/50 focus:border-primary-500 focus:ring-primary-500"
      />
      <button
        @click="$emit('remove', index)"
        class="text-red-500 hover:text-red-700"
        title="Remove parameter"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
        </svg>
      </button>
    </div>
  </div>
</template>