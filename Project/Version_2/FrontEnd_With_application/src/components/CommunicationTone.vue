<script setup lang="ts">
import { ref } from 'vue';
import PersonalityOption from './PersonalityOption.vue';

const props = defineProps<{
  personalities: Array<{ name: string; image: string; description: string }>;
  selectedPersonality: string;
  customPersonality: string;
  creativity: number;
  creativityDescription: string;
  showAdvancedToneOptions: boolean;
  motivationalLevel: number;
  motivationalDescription: string;
  kindnessLevel: number;
  kindnessDescription: string;
  humorLevel: number;
  humorDescription: string;
  useEmojis: boolean;
  emojiFrequency: number;
  emojiDescription: string;
}>();

const emit = defineEmits<{
  (e: 'update:selectedPersonality', value: string): void;
  (e: 'update:customPersonality', value: string): void;
  (e: 'update:creativity', value: number): void;
  (e: 'update:showAdvancedToneOptions', value: boolean): void;
  (e: 'update:motivationalLevel', value: number): void;
  (e: 'update:kindnessLevel', value: number): void;
  (e: 'update:humorLevel', value: number): void;
  (e: 'update:useEmojis', value: boolean): void;
  (e: 'update:emojiFrequency', value: number): void;
}>();

const selectPersonality = (personality: string) => {
  emit('update:selectedPersonality', personality);
  if (personality !== 'Custom') {
    emit('update:customPersonality', '');
  }
};

const updateAdvancedOptions = (value: boolean) => {
  emit('update:showAdvancedToneOptions', value);
};
</script>

<template>
  <div class="glass-effect rounded-xl p-6 card-hover">
    <div class="flex justify-between items-center mb-4">
      <label class="block text-lg font-medium text-gray-700">
        Communication Tone
        <span class="text-gray-500 text-sm ml-2">Select a personality style</span>
      </label>
      <label class="flex items-center space-x-2">
        <span class="text-sm text-gray-600">Advanced</span>
        <input 
          type="checkbox" 
          :checked="showAdvancedToneOptions" 
          @change="updateAdvancedOptions(!showAdvancedToneOptions)" 
          class="toggle-theme" 
        />
      </label>
    </div>
    
    <!-- Personality Selection -->
    <div class="grid grid-cols-2 sm:grid-cols-3 gap-4 mb-6">
      <div
        v-for="personality in personalities"
        :key="personality.name"
        @click="selectPersonality(personality.name)"
      >
        <PersonalityOption
          :name="personality.name"
          :image="personality.image"
          :description="personality.description"
          :selected="selectedPersonality === personality.name"
        />
      </div>
    </div>
    
    <!-- Custom Personality Input -->
    <div v-if="selectedPersonality === 'Custom'" class="mt-4 mb-6">
      <input
        type="text"
        :value="customPersonality"
        @input="emit('update:customPersonality', ($event.target as HTMLInputElement).value)"
        placeholder="Enter personality name (e.g., Shakespeare, Einstein)"
        class="w-full rounded-lg border-gray-300 focus:border-primary-500 focus:ring-primary-500 bg-white/50"
      />
    </div>
    
    <!-- Creativity Slider (Now inside the Communication Tone section) -->
    <div class="mb-6">
      <label class="block text-md font-medium text-gray-700 mb-2">
        Creativity Level
      </label>
      <div class="relative">
        <div class="flex justify-between items-center mb-1">
          <span class="text-xs text-gray-500">Low</span>
          <span class="text-xs text-gray-500">Medium</span>
          <span class="text-xs text-gray-500">High</span>
          <span class="text-xs text-gray-500">Wizard</span>
        </div>
        <input
          type="range"
          :value="creativity"
          @input="emit('update:creativity', parseInt(($event.target as HTMLInputElement).value))"
          min="1"
          max="10"
          class="w-full slider-theme"
        />
      </div>
      <div class="mt-2 text-sm text-gray-500 text-center">
        {{ creativity }}/10 — <span class="font-semibold">{{ creativityDescription }}</span>
      </div>
    </div>
    
    <!-- NEW: Emoji Toggle and Slider -->
    <div class="mb-6">
      <div class="flex justify-between items-center mb-2">
        <label class="block text-md font-medium text-gray-700">
          Include Emojis 🎯
        </label>
        <label class="flex items-center space-x-2">
          <input 
            type="checkbox" 
            :checked="useEmojis" 
            @change="emit('update:useEmojis', !useEmojis)" 
            class="toggle-theme" 
          />
        </label>
      </div>
      <div v-if="useEmojis" class="mt-2">
        <div class="flex justify-between items-center mb-1">
          <span class="text-xs text-gray-500">Minimal 😊</span>
          <span class="text-xs text-gray-500">Moderate 😊🌟</span>
          <span class="text-xs text-gray-500">Abundant 😊🌟🎉</span>
        </div>
        <input
          type="range"
          :value="emojiFrequency"
          @input="emit('update:emojiFrequency', parseInt(($event.target as HTMLInputElement).value))"
          min="1"
          max="10"
          class="w-full slider-theme"
        />
        <div class="mt-2 text-sm text-gray-500 text-center">
          {{ emojiFrequency }}/10 — <span class="font-semibold">{{ emojiDescription }}</span>
        </div>
      </div>
    </div>
    
    <!-- Advanced Tone Sliders (appear when advanced is toggled) -->
    <div v-if="showAdvancedToneOptions" class="mt-4 p-4 border-t space-y-6">
      <h3 class="font-medium text-gray-700">Advanced Tone Controls</h3>
      
      
      <!-- Motivational Level Slider -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">
          Motivational Level 🚀
        </label>
        <input
          type="range"
          :value="motivationalLevel"
          @input="emit('update:motivationalLevel', parseInt(($event.target as HTMLInputElement).value))"
          min="1"
          max="10"
          class="w-full slider-theme"
        />
        <div class="flex justify-between text-xs text-gray-500 mt-1">
          <span>Neutral</span>
          <span>Encouraging</span>
          <span>Inspirational</span>
        </div>
        <div class="mt-1 text-sm text-gray-500 text-center">
          {{ motivationalLevel }}/10 — <span class="font-semibold">{{ motivationalDescription }}</span>
        </div>
      </div>
      
      <!-- Kindness Level Slider -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">
          Kindness Level 💖
        </label>
        <input
          type="range"
          :value="kindnessLevel"
          @input="emit('update:kindnessLevel', parseInt(($event.target as HTMLInputElement).value))"
          min="1"
          max="10"
          class="w-full slider-theme"
        />
        <div class="flex justify-between text-xs text-gray-500 mt-1">
          <span>Direct</span>
          <span>Friendly</span>
          <span>Warm</span>
        </div>
        <div class="mt-1 text-sm text-gray-500 text-center">
          {{ kindnessLevel }}/10 — <span class="font-semibold">{{ kindnessDescription }}</span>
        </div>
      </div>
      
      <!-- Humor Level Slider -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">
          Humor Level 😂
        </label>
        <input
          type="range"
          :value="humorLevel"
          @input="emit('update:humorLevel', parseInt(($event.target as HTMLInputElement).value))"
          min="1"
          max="10"
          class="w-full slider-theme"
        />
        <div class="flex justify-between text-xs text-gray-500 mt-1">
          <span>Serious</span>
          <span>Light Humor</span>
          <span>Very Funny</span>
        </div>
        <div class="mt-1 text-sm text-gray-500 text-center">
          {{ humorLevel }}/10 — <span class="font-semibold">{{ humorDescription }}</span>
        </div>
      </div>
    </div>
  </div>
</template>