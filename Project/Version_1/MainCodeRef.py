from transformers import pipeline
from config import INTENT_CONFIG, NER_CONFIG, TEMPLATES

class IntentProcessor:
    def __init__(self):
        # Initialize models with config values
        self.classifier = pipeline(
            "zero-shot-classification",
            model=INTENT_CONFIG["model_name"]
        )
        self.ner = pipeline(
            "ner",
            model=NER_CONFIG["model_name"],
            aggregation_strategy=NER_CONFIG["aggregation_strategy"]
        )
    
    def get_intent(self, text):
        result = self.classifier(
            text,
            candidate_labels=INTENT_CONFIG["candidate_labels"],
            multi_label=False
        )
        return self._validate_intent(result)
    
    def _validate_intent(self, result):
        top_intent = result["labels"][0]
        top_score = result["scores"][0]
        
        print("\n=== Intent Classification ===")
        print(f"Top Intent: {top_intent} (Score: {top_score:.2f})")
        
        if top_score < INTENT_CONFIG["threshold"]:
            return "general"
        return top_intent
    
    def get_entities(self, text, intent):
        raw_entities = self.ner(text)
        mapped_entities = self._map_entities(raw_entities)
        return self._filter_entities(intent, mapped_entities)

    def _map_entities(self, entities):
        mapped = []
        for ent in entities:
            # Handle different NER model output formats
            entity_group = ent.get("entity_group") or ent.get("entity")
            word = ent.get("word") or ent.get("text")
            
            if entity_group in NER_CONFIG["entity_map"]:
                mapped.append({
                    "text": word.strip(),
                    "type": NER_CONFIG["entity_map"][entity_group],
                    "score": ent["score"]
                })
            else:
                print(f"Unmapped entity: {entity_group} ({word})")
        return mapped

    def _filter_entities(self, intent, entities):
        keep_types = NER_CONFIG["intent_filters"].get(intent, [])
        return {
            "allEntities":[e for e in entities],
            "relevant": [e for e in entities if e["type"] in keep_types],
            "irrelevant": [e for e in entities if e["type"] not in keep_types]
        }
    def _has_required_data(self, template, entities):
        """Check if template's required fields have entity data"""
        required_fields = template.get("fields", [])
        entity_types = [e["type"] for e in entities["relevant"]]
        print(f"Required Fields: {required_fields}")
        # entity_types = [e["type"] for e in entities["relevant"]]
        # Check if at least 50% of required fields are present
        matched = sum(1 for field in required_fields if field in entity_types)
        print(f"====== Required Data Check ======{matched}")
        print(len(required_fields))
        return matched / len(required_fields) >= 0.5
    
    def get_template(self, intent, entities):
        """Resolve template with fallback logic"""
        template = None
        print(f"\n======Finding Template with the intent: {intent}")
        if intent in TEMPLATES:
            template = TEMPLATES[intent].get("advanced", TEMPLATES[intent]["default"])
        else:
            template = TEMPLATES[intent].get("default", TEMPLATES[intent]["default"])
        return template

        # 1. Check specialized intent templates
        # if intent in TEMPLATES and "default" in TEMPLATES[intent]:
        # if intent in TEMPLATES:
        #     # Template selection logic
        #     template = TEMPLATES[intent].get("advanced", TEMPLATES[intent]["default"])
        #     # if self._has_required_data(template, entities):
        #     return template
        
        # # 2. Check general intent templates
        # if "general" in TEMPLATES and intent in TEMPLATES["general"]:
        #     template = TEMPLATES["general"][intent]
        #     if self._has_required_data(template, entities):
        #         return template
        
        # # 3. Fallback to default
        # return TEMPLATES["general"]["default"] - v1


    
    def extract_domains(self, entities):
        return [e["text"] for e in entities["allEntities"] if "domain" in e["type"].lower() or "*general*" in e["type"].lower()]

    def generate_prompt(self, intent, filtered_entities):
        # Get template or fallback to general
        
        # template = TEMPLATES.get(intent[intent]) - v1
        template = self.get_template(intent, filtered_entities)
        domains = self.extract_domains(filtered_entities)
        tools = [
            e["text"] for e in filtered_entities["allEntities"]
            if "tool" in e["type"].lower()
        ]
        # Auto-populate template fields
        formatted_header = template["header"].format(domain=", ".join(domains),experience="10+")  # Consider parameterizing this)
        components = {
            "header": formatted_header,
            "fields": template["fields"]
        }
    
        # # Build components
        # components = {
        #     "header": header,
        #     "fields": {
        #         "domains": domains,
        #         "tools": tools,
        #         "other": [
        #             e["text"] for e in filtered_entities["relevant"]
        #             if "domain" not in e["type"].lower() and "tool" not in e["type"].lower()
        #         ]
        #     }
        # } - v1
        
        return components

# Usage
if __name__ == "__main__":
    processor = IntentProcessor()
    
    user_input = input("Enter your request: ")
    
    # Get intent
    intent = processor.get_intent(user_input)
    
    # Get entities
    # entities = processor.get_entities(user_input) - v1
    entities = processor.get_entities(user_input, intent)

    print(entities["relevant"])
    
    # Generate prompt components
    prompt = processor.generate_prompt(intent, entities)
    
    print("\n=== Generated Prompt Components ===")
    print(f"Intent: {intent}")
    print(f"Header: {prompt['header']}")
    print(f"Required Fields: {prompt['fields']}")
    print(f"Detected Entities: {entities}")