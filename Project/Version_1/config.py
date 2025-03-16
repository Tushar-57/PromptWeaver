# config.py
from transformers import pipeline

# Intent classification config
INTENT_CONFIG = {
    "model_name": "MoritzLaurer/deberta-v3-base-zeroshot-v1",
    
    "candidate_labels": [
        "learn", "explain", "understand", "teach", "what is", "define", 
        "describe", "overview", "introduction", "basics", "fundamentals",
        "summarize", "brief", "condensed", "compare", "analyze", "write", 
        "howto", "persuade", "argue", "recommend", "troubleshoot", "plan", 
        "research", "code", "translate", "brainstorm", "decide", "story"
    ],
    "threshold": 0.7
}

# NER config - V1
# NER_CONFIG = {
#     "model_name": "Jean-Baptiste/roberta-large-ner-english",
#     "aggregation_strategy": "simple",
#     "entity_groups": {
#         "ORG": "Technology",
#         "MISC": "Domain",
#         "PER": "Person",
#         "LOC": "Tool"
#     }
# }
#NER Config - V2
NER_CONFIG = {
    "model_name": "Jean-Baptiste/roberta-large-ner-english",
    "aggregation_strategy": "simple",
    "entity_map": {
        # Original model outputs
        # "PER": "Person/Character",
        # "ORG": "Technology/Company",
        # "LOC": "Tool/Location",
        # "MISC": "Domain/Concept",   V1
        "PER": "Person/Character",
        "ORG": "Technology/Company",
        "LOC": "Tool/Location", 
        "MISC": "Domain/Concept",
        "TECH": "Technology/Company",
        "DOM": "Domain/Concept",
        
        # Custom extensions
        "TOOL": "Tool",
        "ERR": "Error",
        "SKILL": "SkillLevel",
        "TIME": "Timeframe",
        "LANG": "ProgrammingLanguage",
        "FRAMEWORK": "Framework"
    },
    "intent_filters": {
        "learn": ["DOM", "TECH", "TOOL", "SKILL"],
        "explain": ["DOM", "TECH", "CONCEPT"],
        "compare": ["TECH", "TOOL", "PRODUCT"],
        "troubleshoot": ["TOOL", "ERR", "PLATFORM"],
        "plan": ["DOM", "TECH", "TIME"],
        "research": ["DOM", "TECH", "CONCEPT"],
        "code": ["LANG", "FRAMEWORK", "TOOL"],
        "translate": ["LANG", "CONTENT"],
        "story": ["PER", "LOC", "EVENT"]
    }
}

# Template config
TEMPLATES = {
    "general": {
        "default": {
            "header": "You are a general assistant helping with {domain}",
            "fields": ["ORG","MISC"]
        },
        "learn": {
            "header": "You are an experienced {domain} coach with {experience} years experience",
            "fields": ["current_level", "learning_style", "time_commitment"]
        },
        "compare": {
            "header": "Technical comparison expert specializing in {domain}",
            "fields": ["subject1", "subject2", "comparison_aspects"]
        }
    },
    "learn": {
        "default": {
            "header": "You are a knowledgeable assistant in the domain of {domain}, and will be helping me with {domain}",
            "fields": ["MISC"]
        },
        "advanced": {
            "header": "You are a knowledgeable assistant helping with {domain}",
            "fields": ["ORG", "MISC", "TECH"]
        }
    }
}