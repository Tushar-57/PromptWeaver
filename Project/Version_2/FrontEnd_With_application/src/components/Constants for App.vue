<script setup lang="ts">
const personalities = [
  {
    name: 'Professional',
    image: '/images/professional.jpg',
    description: 'Clear, concise, and business-oriented responses'
  },
  {
    name: 'Creative',
    image: '/images/creative.jpg',
    description: 'Imaginative and artistic with fresh perspectives'
  },
  {
    name: 'Academic',
    image: '/images/academic.jpg',
    description: 'Scholarly analysis with citations and depth'
  },
  {
    name: 'Friendly',
    image: '/images/friendly.jpg',
    description: 'Warm, approachable, and conversational'
  },
  {
    name: 'Technical',
    image: '/images/technical.jpg',
    description: 'Precise technical details with expert terminology'
  },
  {
    name: 'Custom',
    image: '/images/custom.jpg',
    description: 'Define your own personality style'
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
</script>