import re
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from collections import OrderedDict

class InteractivePromptGenerator:
    def __init__(self, model_name="EleutherAI/gpt-neo-125M"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        
        # Templates and configuration
        self.templates = OrderedDict([
            ("general", "Explain {task} using {complexity} complexity."),
            ("creative", "Write {content_type} about {topic} with {tone} tone."),
            ("analytical", "Analyze {subject} focusing on {aspects}."),
            ("instructional", "Create {step_count}-step guide for {task}."),
            ("summarization", "Summarize {topic} in {summary_length} words.")
        ])
        
        # Developer mode controls
        self.dev_mode = False
        self.manual_params = {}
        self.available_controls = {
            'intent': list(self.templates.keys()) + ['custom'],
            'tone': ['neutral', 'professional', 'casual', 'humorous', 'sarcastic'],
            'complexity': ['simple', 'moderate', 'complex'],
            'strictness': ['strict', 'moderate', 'lenient'],
            'style': ['concise', 'detailed', 'technical', 'storytelling']
        }

    def interactive_dev_mode(self):
        """Start interactive developer console"""
        print("\n=== DEVELOPER MODE ACTIVATED ===")
        print("Configure parameters (press Enter to skip):")
        
        # Intent selection
        self._print_options("Intent Type", self.available_controls['intent'])
        choice = self._get_choice(len(self.available_controls['intent']))
        if choice is not None:
            selected_intent = self.available_controls['intent'][choice]
            if selected_intent == 'custom':
                self.templates['custom'] = input("Enter custom template: ")
            self.manual_params['intent'] = selected_intent

        # Tone selection
        self._print_options("Tone", self.available_controls['tone'])
        choice = self._get_choice(len(self.available_controls['tone']))
        if choice is not None:
            self.manual_params['tone'] = self.available_controls['tone'][choice]

        # Complexity level
        self._print_options("Complexity", self.available_controls['complexity'])
        choice = self._get_choice(len(self.available_controls['complexity']))
        if choice is not None:
            self.manual_params['complexity'] = self.available_controls['complexity'][choice]

        print("\nDeveloper Configuration Complete!")
        print(f"Active Parameters: {self.manual_params}\n")

    def _print_options(self, title, options):
        """Display options with numbering"""
        print(f"\n{title}:")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option.capitalize()}")
            
    def _get_choice(self, max_options):
        """Get validated user choice"""
        while True:
            try:
                choice = input("Select (1-{}): ".format(max_options))
                if not choice: return None
                choice_idx = int(choice) - 1
                if 0 <= choice_idx < max_options:
                    return choice_idx
                print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a number.")

    def generate_prompt(self, user_input):
        """Generate prompt with developer controls"""
        # Apply developer parameters
        intent = self.manual_params.get('intent', self._detect_intent(user_input))
        entities = self._extract_entities(user_input, intent)
        entities.update({k:v for k,v in self.manual_params.items() if k != 'intent'})
        
        # Select template
        template = self.templates.get(intent, self.templates['general'])
        
        # Format prompt
        try:
            return template.format(**entities)
        except KeyError as e:
            return self._handle_format_error(template, entities)
            
    def _detect_intent(self, user_input):
        """Auto-detect intent if not specified"""
        # Simplified intent detection logic
        if 'write' in user_input.lower(): return 'creative'
        if 'analyze' in user_input.lower(): return 'analytical'
        if 'step' in user_input.lower(): return 'instructional'
        if 'summar' in user_input.lower(): return 'summarization'
        return 'general'

    def _extract_entities(self, user_input, intent):
        """Basic entity extraction"""
        entities = {}
        if intent == 'creative':
            entities['content_type'] = 'a ' + ('story' if 'story' in user_input else 'text')
            entities['topic'] = user_input.split('about')[-1].split('with')[0].strip()
        elif intent == 'instructional':
            entities['step_count'] = 5  # Default steps
            entities['task'] = user_input.split('guide')[-1].strip()
        return entities

    def _handle_format_error(self, template, entities):
        """Handle missing format parameters"""
        missing = re.findall(r'\{(.*?)\}', template)
        print(f"Missing parameters: {missing}")
        return "Could not generate prompt - missing parameters"

# Testing Interface
if __name__ == "__main__":
    generator = InteractivePromptGenerator()
    
    # Activate interactive developer mode
    generator.interactive_dev_mode()
    
    # Test input
    while True:
        user_input = input("\nEnter your request (or 'exit'): ")
        if user_input.lower() == 'exit':
            break
            
        print("\nGenerated Prompt:", generator.generate_prompt(user_input))