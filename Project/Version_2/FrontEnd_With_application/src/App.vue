<script setup lang="ts">
import { ref, computed } from 'vue';
import { useClipboard } from '@vueuse/core';
import PersonalityOption from './components/PersonalityOption.vue';
import CustomParameter from './components/CustomParameter.vue';
import CommunicationTone from './components/CommunicationTone.vue';
import axios from 'axios';

const isGenerating = ref(false);
const apiResponse = ref('');

const { copy, copied } = useClipboard();

// Personality options data
const personalities = [
  {
    name: 'Elon Musk',
    image: 'https://upload.wikimedia.org/wikipedia/commons/3/34/Elon_Musk_Royal_Society_%28crop2%29.jpg',
    description: 'Direct, innovative, and sometimes provocative communication style'
  },
  {
    name: 'Donald Trump',
    image: 'https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg',
    description: 'Bold, assertive, and emphatic communication style'
  },
  {
    name: 'IShowSpeed',
    image: 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/IShowSpeed_in_January_2023.png/640px-IShowSpeed_in_January_2023.png',
    description: 'Wise, measured, and analytical communication style'
  },
  {
    name: 'Mark Zuckerberg',
    image: 'https://upload.wikimedia.org/wikipedia/commons/1/18/Mark_Zuckerberg_F8_2019_Keynote_%2832830578717%29_%28cropped%29.jpg',
    description: 'Technical, data-driven, and future-focused communication style'
  },
  {
    name: 'David Goggins',
    image: 'https://upload.wikimedia.org/wikipedia/commons/e/e3/DavidGogginsMay08.jpg',
    description: 'Motivational speaker, author, and retired United States Navy SEAL'
  },
  {
    name: 'Custom',
    image: 'https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png',
    description: 'Add your own personality'
  }
];

// Output format options
const outputFormats = [
  {
    label: 'Paragraph',
    value: 'paragraph',
    details: [
      { label: 'Standard', value: 'standard' },
      { label: 'Persuasive', value: 'persuasive' },
      { label: 'Descriptive', value: 'descriptive' }
    ]
  },
  {
    label: 'Bullet Points',
    value: 'bullets',
    details: [
      { label: 'Concise', value: 'concise' },
      { label: 'Detailed', value: 'detailed' },
      { label: 'Hierarchical', value: 'hierarchical' }
    ]
  },
  {
    label: 'Step by Step',
    value: 'steps',
    details: [
      { label: 'Numbered', value: 'numbered' },
      { label: 'Guided', value: 'guided' },
      { label: 'Tutorial', value: 'tutorial' }
    ]
  },
  {
    label: 'Q&A Format',
    value: 'qa',
    details: [
      { label: 'Interview', value: 'interview' },
      { label: 'FAQ', value: 'faq' },
      { label: 'Socratic', value: 'socratic' }
    ]
  }
];

// Response length options
const responseLengths = [
  {
    label: 'Brief',
    value: 'brief',
    description: 'Short and concise',
    details: [
      { label: 'Minimal (1-2 sentences)', value: 'minimal' },
      { label: 'Quick summary', value: 'summary' },
      { label: 'Key points only', value: 'key_points' }
    ]
  },
  {
    label: 'Balanced',
    value: 'balanced',
    description: 'Moderate length',
    details: [
      { label: 'Conversational', value: 'conversational' },
      { label: 'Detailed enough', value: 'standard' },
      { label: 'Clear explanations', value: 'explanatory' }
    ]
  },
  {
    label: 'Detailed',
    value: 'detailed',
    description: 'Comprehensive',
    details: [
      { label: 'In-depth analysis', value: 'analysis' },
      { label: 'Thorough exploration', value: 'thorough' },
      { label: 'Complete coverage', value: 'complete' }
    ]
  }
];

// Existing state
const basePrompt = ref('');
const selectedPersonality = ref('Elon Musk');
const customPersonality = ref('');
const creativity = ref(2); // Range 1 to 10
const outputFormat = ref('steps');
const selectedFormatDetail = ref('');
const responseLength = ref('balanced');
const selectedLengthDetail = ref('');
const context = ref('');
const customParams = ref<{ key: string; value: string }[]>([]);

// Advanced toggle states per section - updated to be independent
const showAdvancedToneOptions = ref(false);
const showAdvancedOutputOptions = ref(false);
const showAdvancedLengthOptions = ref(false);
const showAdvancedContextOptions = ref(false);
const showAdvancedCustomParams = ref(false);

// New advanced tone sliders
const motivationalLevel = ref(5); // Range 1 to 10
const kindnessLevel = ref(5); // Range 1 to 10
const humorLevel = ref(5); // Range 1 to 10
const useEmojis = ref(false);
const emojiFrequency = ref(3); // Range 1 to 10

// Computed mapping for creativity descriptive labels
const creativityDescription = computed(() => {
  if (creativity.value <= 3) return 'Factual and straightforward';
  if (creativity.value <= 6) return 'Balanced mix of creativity';
  if (creativity.value < 10) return 'Highly imaginative';
  return 'Creative Wizard';
});

// Computed descriptions for advanced tone sliders
const motivationalDescription = computed(() => {
  if (motivationalLevel.value <= 3) return 'Neutral tone';
  if (motivationalLevel.value <= 6) return 'Encouraging';
  if (motivationalLevel.value < 10) return 'Highly motivational';
  return 'Extremely inspirational';
});

const kindnessDescription = computed(() => {
  if (kindnessLevel.value <= 3) return 'Direct and straightforward';
  if (kindnessLevel.value <= 6) return 'Friendly and approachable';
  if (kindnessLevel.value < 10) return 'Warm and supportive';
  return 'Extremely empathetic and kind';
});

const humorDescription = computed(() => {
  if (humorLevel.value <= 3) return 'Serious tone';
  if (humorLevel.value <= 6) return 'Light humor';
  if (humorLevel.value < 10) return 'Quite funny';
  return 'Very humorous';
});

const emojiDescription = computed(() => {
  if (emojiFrequency.value <= 3) return 'Minimal emojis';
  if (emojiFrequency.value <= 6) return 'Moderate emoji use';
  if (emojiFrequency.value < 10) return 'Frequent emojis';
  return 'Abundant emojis';
});

// Generate the prompt based on all selected options
const generatedPrompt = computed(() => {
  let prompt = `Base prompt: ${basePrompt.value}\n\n`;
    
  // Personality and tone
  prompt += `Personality: ${selectedPersonality.value === 'Custom' ? customPersonality.value : selectedPersonality.value}\n`;
  prompt += `Creativity: ${creativity.value}/10 (${creativityDescription.value})\n`;
  
  // Advanced tone options
  if (showAdvancedToneOptions.value) {
    prompt += `Motivation Level: ${motivationalLevel.value}/10 (${motivationalDescription.value})\n`;
    prompt += `Kindness Level: ${kindnessLevel.value}/10 (${kindnessDescription.value})\n`;
    prompt += `Humor Level: ${humorLevel.value}/10 (${humorDescription.value})\n`;
  }
  
  // Emoji settings
  if (useEmojis.value) {
    prompt += `Use emojis: Yes - ${emojiFrequency.value}/10 (${emojiDescription.value})\n`;
  }
  
  // Output format
  prompt += `Format: ${outputFormat.value}${selectedFormatDetail.value ? ` (${selectedFormatDetail.value})` : ''}\n`;
  
  // Response length
  prompt += `Length: ${responseLength.value}${selectedLengthDetail.value ? ` (${selectedLengthDetail.value})` : ''}\n`;
  
  // Context if provided
  if (context.value) {
    prompt += `\nContext:\n${context.value}\n`;
  }
  
  // Custom parameters
  if (customParams.value.length > 0) {
    prompt += `\nCustom Parameters:\n`;
    customParams.value.forEach(param => {
      prompt += `${param.key}: ${param.value}\n`;
    });
  }
  
  return prompt;
});

// Helper functions
const addCustomParam = () => {
  customParams.value.push({ key: '', value: '' });
};

const removeCustomParam = (index: number) => {
  customParams.value.splice(index, 1);
};

const updateCustomParam = (index: number, key: string, value: string) => {
  customParams.value[index] = { key, value };
};

const handleContextDrop = (e: DragEvent) => {
  e.preventDefault();
  const file = e.dataTransfer?.files[0];
  if (file) {
    const reader = new FileReader();
    reader.onload = (e) => {
      context.value = e.target?.result as string;
    };
    reader.readAsText(file);
  }
};

const selectPersonality = (personality: string) => {
  selectedPersonality.value = personality;
  if (personality !== 'Custom') {
    customPersonality.value = '';
  }
};

// Reset Scrript
const resetForm = () => {
  basePrompt.value = '';
  selectedPersonality.value = '';
  customPersonality.value = '';
  creativity.value = 5;
  outputFormat.value = 'paragraph';
  selectedFormatDetail.value = '';
  responseLength.value = 'balanced';
  selectedLengthDetail.value = '';
  context.value = '';
  customParams.value = [];
  motivationalLevel.value = 5;
  kindnessLevel.value = 5;
  humorLevel.value = 5;
  useEmojis.value = false;
  emojiFrequency.value = 3;
  showAdvancedToneOptions.value = false;
  showAdvancedOutputOptions.value = false;
  showAdvancedLengthOptions.value = false;
  showAdvancedContextOptions.value = false;
  showAdvancedCustomParams.value = false;
};
const generateResponse = async () => {
  isGenerating.value = true;
  try {
    const response = await axios.post('http://localhost:5000/generate', {
      // Send structured data (recommended)
      config: {
        base_prompt: basePrompt.value,
        personality: selectedPersonality.value,
        creativity: creativity.value,
        output_format: outputFormat.value,
        custom_params: customParams.value,
        custom_personality:customPersonality.value,
        selected_format_detail:selectedFormatDetail.value,
        response_length : responseLength.value,
        selected_length : selectedLengthDetail.value,
        context:context.value,
        motivation : motivationalLevel.value,
        kindness:kindnessLevel.value,
        humor:humorLevel.value,
        use_emoji:useEmojis.value,
        emoji_freq:emojiFrequency.value
        // Include all other relevant fields
      },
      // Or send the generated prompt text
      // prompt: generatedPrompt.value
    });
    
    apiResponse.value = response.data.assistant_response || 'No response received';
  } catch (error) {
    console.error('API Error:', error);
    apiResponse.value = 'Error: ' + (error.message || 'Failed to get response');
    alert('Generation failed');
  } finally {
    isGenerating.value = false;
  }
};
</script>
<template>
  <div class="relative min-h-screen">
    <!-- Floating Reset Button -->
    <button @click="resetForm"
      class="fixed right-4 top-1/2 -translate-y-1/2 z-50 px-6 py-3 bg-gradient-to-br from-primary-500 via-pink-500 to-purple-600 text-white rounded-full shadow-xl hover:shadow-2xl transition-all duration-300 transform hover:scale-105 font-bold flex items-center space-x-2 border-2 border-white/20 hover:border-white/40"
      style="backdrop-filter: blur(10px)">
      <span class="text-lg animate-spin-on-hover">🔄</span>
      <span class="hidden sm:inline-block">Reset All</span>
    </button>
    </div>

    <!-- Content container -->
    <div class="py-12 px-4 sm:px-6 lg:px-8">
      <div class="max-w-4xl mx-auto">
        <!-- Preset buttons -->
        <div class="flex gap-4 mb-8">
          <button
            v-for="preset in ['Academic Paper', 'Social Media', 'Business Proposal']"
            @click="loadPreset(preset)"
            class="px-4 py-2 rounded-full bg-white/50 hover:bg-primary-100 text-sm font-medium"
          >
            {{ preset }} 
            <span class="ml-1 text-primary-500">★</span>
          </button>
          <button
            @click="savePreset"
            class="px-4 py-2 rounded-full bg-primary-100 hover:bg-primary-200 text-sm font-medium"
          >
            + Save Current
          </button>
        </div>

        <!-- Main content -->
        <h1 class="text-5xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-primary-600 to-pink-600 text-center mb-4 float-animation">
          Prompt Weaver 
        </h1>
        <p class="text-center text-gray-600 mb-12 text-lg">
          Transform your ideas into perfectly crafted prompts with personality-driven AI responses ✨
        </p>

        <!-- Form sections -->
        <div class="space-y-8">
          <!-- Base Prompt Section -->
          <div class="glass-effect rounded-xl p-6 card-hover">
            <label for="base-prompt" class="block text-lg font-medium text-gray-700 mb-2">
              🌟 Base Prompt (Hint: Think Like a Human and Leave Rest to Us ! )
            </label>
            <textarea
              id="base-prompt"
              v-model="basePrompt"
              rows="4"
              class="w-full rounded-lg border-gray-300 focus:border-primary-500 focus:ring-0 focus:shadow-[0_0_0_2px_rgba(139,92,246,0.2)] bg-white/50"
              placeholder="Example: Prompt for Learing AI, Prompt for Roadmap"
            ></textarea>
          </div>
        <!-- RESTRUCTURED Communication Tone Section with Creativity -->
        <CommunicationTone
          :personalities="personalities"
          :selected-personality="selectedPersonality"
          :custom-personality="customPersonality"
          :creativity="creativity"
          :creativity-description="creativityDescription"
          :show-advanced-tone-options="showAdvancedToneOptions"
          :motivational-level="motivationalLevel"
          :motivational-description="motivationalDescription"
          :kindness-level="kindnessLevel"
          :kindness-description="kindnessDescription"
          :humor-level="humorLevel"
          :humor-description="humorDescription"
          :use-emojis="useEmojis"
          :emoji-frequency="emojiFrequency"
          :emoji-description="emojiDescription"
          @update:selected-personality="selectedPersonality = $event"
          @update:custom-personality="customPersonality = $event"
          @update:creativity="creativity = $event"
          @update:show-advanced-tone-options="showAdvancedToneOptions = $event"
          @update:motivational-level="motivationalLevel = $event"
          @update:kindness-level="kindnessLevel = $event"
          @update:humor-level="humorLevel = $event"
          @update:use-emojis="useEmojis = $event"
          @update:emoji-frequency="emojiFrequency = $event"
        />
        <!-- Add as new card component -->
        <div class="glass-effect rounded-xl p-6 card-hover">
          <label class="block text-lg font-medium text-gray-700 mb-4">
            Audience Profile
          </label>
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-gray-700">Age Group</label>
              <input
                type="range"
                min="1"
                max="5"
                :value="audienceAge"
                @input="emit('update:audienceAge', $event.target.value)"
                class="w-full slider-theme mt-2"
              >
              <div class="flex justify-between text-xs text-gray-500 mt-1">
                <span>Children</span>
                <span>Teens</span>
                <span>Adults</span>
                <span>Seniors</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Output Format Section -->
        <div class="glass-effect rounded-xl p-6 card-hover relative">
          <div class="flex justify-between items-center mb-4">
            <label class="block text-lg font-medium text-gray-700">
              Output Format
            </label>
            <label class="flex items-center space-x-2">
              <span class="text-sm text-gray-600">Advanced</span>
              <input type="checkbox" v-model="showAdvancedOutputOptions" class="toggle-theme" />
            </label>
          </div>
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-4">
            <div
              v-for="format in outputFormats"
              :key="format.value"
              class="space-y-2"
            >
              <button
                @click="outputFormat = format.value"
                class="w-full px-4 py-2 rounded-lg transition-all"
                :class="outputFormat === format.value ? 'bg-primary-500 text-white' : 'bg-white/50 hover:bg-white/80 text-gray-700'"
              >
                {{ format.label }}
              </button>
              <div v-if="showAdvancedOutputOptions && outputFormat === format.value" class="bg-white/50 rounded-lg p-2">
                <div
                  v-for="detail in format.details"
                  :key="detail.value"
                  class="cursor-pointer text-sm p-1 hover:bg-primary-100 rounded"
                  :class="{ 'bg-primary-200 font-bold': selectedFormatDetail === detail.value }"
                  @click="selectedFormatDetail = detail.value"
                >
                  {{ detail.label }}
                </div>
              </div>
              <div class="mt-2">
            </div>
          </div>
          <label class="block text-sm font-medium text-gray-700">
                Narrative Perspective
              </label>
              <select
                :value="narrativePerspective"
                @change="emit('update:narrativePerspective', $event.target.value)"
                class="w-full mt-1 rounded-lg border-gray-300"
              >
                <option value="first">First Person (I/We)</option>
                <option value="second">Second Person (You)</option>
                <option value="third">Third Person (They)</option>
              </select>
            </div>
        </div>

        <!-- Response Length Section -->
        <div class="glass-effect rounded-xl p-6 card-hover relative">
          <div class="flex justify-between items-center mb-4">
            <label class="block text-lg font-medium text-gray-700">
              Response Length
            </label>
            <label class="flex items-center space-x-2">
              <span class="text-sm text-gray-600">Advanced</span>
              <input type="checkbox" v-model="showAdvancedLengthOptions" class="toggle-theme" />
            </label>
          </div>
          <div class="flex gap-4">
            <div
              v-for="length in responseLengths"
              :key="length.value"
              class="flex-1 space-y-2 p-2 rounded-lg border transition-all cursor-pointer"
              :class="responseLength === length.value ? 'bg-primary-500 text-white shadow-lg' : 'bg-white/50 hover:bg-white/80 text-gray-700'"
              @click="responseLength = length.value"
            >
              <div class="text-lg font-semibold text-center">{{ length.label }}</div>
              <div class="text-xs text-center">{{ length.description }}</div>
            </div>
          </div>
          <div v-if="showAdvancedLengthOptions" class="mt-4 p-4 border-t">
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
              <div
                v-for="length in responseLengths"
                :key="length.value"
                v-show="responseLength === length.value"
                class="bg-white/50 rounded-lg p-2"
              >
                <div class="text-sm font-medium mb-2">Detail level for {{ length.label }}</div>
                <div
                  v-for="detail in length.details"
                  :key="detail.value"
                  class="cursor-pointer p-1 rounded hover:bg-primary-100"
                  :class="{ 'bg-primary-200 font-bold': selectedLengthDetail === detail.value }"
                  @click="selectedLengthDetail = detail.value"
                >
                  {{ detail.label }}
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Context Section -->
        <div class="glass-effect rounded-xl p-6 card-hover">
          <div class="flex justify-between items-center mb-2">
            <label class="block text-lg font-medium text-gray-700">
              Context
            </label>
            <label class="flex items-center space-x-2">
              <span class="text-sm text-gray-600">Advanced</span>
              <input type="checkbox" v-model="showAdvancedContextOptions" class="toggle-theme" />
            </label>
          </div>
          <div
            class="border-2 border-dashed border-gray-300 rounded-lg p-6 text-center bg-white/50"
            @drop="handleContextDrop"
            @dragover.prevent
          >
            <textarea
              v-model="context"
              rows="3"
              class="w-full bg-transparent focus:outline-none"
              placeholder="Drag and drop a file here or paste your context..."
            ></textarea>
          </div>
          <div v-if="showAdvancedContextOptions" class="mt-4 p-4 border-t">
            <p class="text-sm text-gray-500 mb-2">
              Advanced context options:
            </p>
            <div class="space-y-3">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">
                  Context Analysis Level
                </label>
                <select class="w-full p-2 rounded-lg border bg-white/50">
                  <option value="basic">Basic (Extract key points)</option>
                  <option value="normal">Normal (Standard analysis)</option>
                  <option value="deep">Deep (In-depth analysis)</option>
                </select>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">
                  Additional Context URL
                </label>
                <input type="text" placeholder="https://example.com/resource" class="w-full p-2 rounded-lg border bg-white/50" />
              </div>
            </div>
          </div>
        </div>

        <!-- Custom Parameters Section -->
        <div class="glass-effect rounded-xl p-6 card-hover">
          <div class="flex justify-between items-center mb-4">
            <label class="block text-lg font-medium text-gray-700">
              Custom Parameters
            </label>
            <div class="flex items-center">
              <label class="flex items-center space-x-2 mr-4">
                <span class="text-sm text-gray-600">Advanced</span>
                <input type="checkbox" v-model="showAdvancedCustomParams" class="toggle-theme" />
              </label>
              <button
                @click="addCustomParam"
                class="text-primary-500 hover:text-primary-700 flex items-center gap-1"
              >
                <span class="text-lg">+</span> Add Parameter
              </button>
            </div>
          </div>
          <div class="space-y-4">
            <CustomParameter
              v-for="(param, index) in customParams"
              :key="index"
              :index="index"
              :param="param"
              @remove="removeCustomParam"
              @update="updateCustomParam"
            />
          </div>
          <div v-if="showAdvancedCustomParams" class="mt-4 p-4 border-t">
            <p class="text-sm text-gray-500 mb-2">
              Advanced custom parameters: Enter parameters as JSON.
            </p>
            <textarea
              placeholder='{"temperature": 0.7, "max_tokens": 150}'
              class="w-full rounded-lg border-gray-300 focus:border-primary-500 focus:ring-primary-500 bg-white/50 p-2"
              rows="3"
            ></textarea>
          </div>
        </div>

        <!-- Generated Prompt Section -->
        <div class="glass-effect rounded-xl p-6 card-hover transform transition-all hover:scale-105">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-lg font-semibold text-transparent bg-clip-text bg-gradient-to-r from-primary-600 to-pink-600">
              ✨ Your Magic Prompt ✨
            </h2>
            <button
              @click="copy(generatedPrompt)"
              class="text-primary-500 hover:text-primary-700 flex items-center gap-2 transition-all hover:scale-110">
              <span>{{ copied ? '🎉 Copied!' : '📋 Copy' }}</span>
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                  d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" 
                />
              </svg>
            </button>
          </div>
          <pre class="whitespace-pre-wrap text-gray-700 bg-white/50 p-4 rounded-lg border-2 border-primary-100 shadow-lg">{{ generatedPrompt }}
          </pre>
        </div>
        <button
        @click="generateResponse"
        :disabled="isGenerating"
        class="ml-4 text-primary-500 hover:text-primary-700 flex items-center gap-2 transition-all hover:scale-110">
        <span>{{ isGenerating ? 'Generating...' : '🚀 Generate' }}</span>
        </button>
        <div class="glass-effect rounded-xl p-6 card-hover transform transition-all hover:scale-105">
          <div class="flex justify-between items-center mb-4">
            <h2 class="text-lg font-semibold text-transparent bg-clip-text bg-gradient-to-r from-primary-600 to-pink-600">
              Your Custom LLM Prompt 🚀🔥
            </h2>
            <button
              @click="copy(generatedPrompt)"
              class="text-primary-500 hover:text-primary-700 flex items-center gap-2 transition-all hover:scale-110">
              <span>{{ copied ? '🎉 Copied!' : '📋 Copy' }}</span>
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" 
                  d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" 
                />
              </svg>
            </button>
          </div>
          <pre class="whitespace-pre-wrap text-gray-700 bg-white/50 p-4 rounded-lg border-2 border-primary-100 shadow-lg">{{ apiResponse }} </pre>
        </div>
          
        <div class="glass-effect rounded-xl p-6 card-hover transform transition-all hover:scale-105">
            <div class="flex justify-between items-center mb-4">
              <h2 class="text-lg font-semibold text-transparent bg-clip-text bg-gradient-to-r from-primary-600 to-pink-600">
                ✨ Future Dev Plan: ✨
              </h2>
              <p>Implementing FrontEnd Model for LLMs.</p><br/>
              <p>Intelligent Multi Agent Framework.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
