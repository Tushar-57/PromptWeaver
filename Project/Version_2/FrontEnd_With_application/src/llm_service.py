from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.models import ModelFactory
from camel.types import ModelPlatformType


def create_model(model_name: str):
    # This function creates your model. For our simulation, we simply return a dummy object.
    model = ModelFactory.create(
        model_platform=ModelPlatformType.OLLAMA,
        model_type=model_name,
        url="http://localhost:11434/v1",  # Optional
        model_config_dict={"temperature": 0.9},
    )
    return model

# Create a singleton model instance.
MODEL_INSTANCE = create_model("llama3.2:3b")

def process_user_request(data: dict, logger) -> (str, dict):
    """
    Process the user request by generating an LLM-ready prompt template that outlines 
    all the user-defined parameters. This prompt is intended to be fed into another LLM.
    """
    config = data.get('config', {})
    
    # Construct the meta-prompt that instructs the target LLM to generate a prompt.
    detailed_prompt = f"""
      You are to generate a prompt that can be used as input for another LLM. Your generated prompt must strictly adhere to the following parameters:

      1. **Base Prompt**: "{config.get('base_prompt', 'custom_personality')}"
         (This is the primary subject or task the user is interested in.)

      2. **Personality & Tone**:  
         - **Personality**: "{config.get('personality', '')}"  
         - The prompt should instruct the LLM to respond in a manner that reflects this personality.  
         - The tone should be engaging, motivational, and confident.

      3. **Creativity Level**: {config.get('creativity', '')}/10  
         (Instruct the LLM to incorporate creative and innovative ideas, while keeping the language clear.)

      4. **Advanced Tone Settings**:  
         - **Motivation Level**: {config.get('motivation', '')}/10  
         - **Kindness Level**: {config.get('kindness', '')}/10  
         - **Humor Level**: {config.get('humor', '')}/10  
         - Instruct the LLM to include emojis as specified:  
            - **Include Emojis**: {config.get('use_emoji', False)}  
            - **Emoji Frequency**: {config.get('emoji_freq', '')}/10

      5. **Audience Profile**:  
         The response should be tailored for an audience of "{config.get('audience_profile', '')}" with an expertise level of "{config.get('expertise_level', '')}".

      6. **Output Format**:  
         Instruct the LLM to generate the response in "{config.get('output_format', '')}" format.  
         If additional details are provided (e.g., "{config.get('selected_format_detail', '')}"), they must be incorporated.

      7. **Response Length**:  
         The response should be "{config.get('response_length', '')}".  
         If specifics are available (e.g., "{config.get('selected_length', '')}"), they must be followed.

      8. **Additional Context**:  
         If provided, the prompt should include the following context: "{config.get('context', '')}"

      9. **Custom Parameters**:  
         {", ".join([f"{p.get('key')}: {p.get('value')}" for p in config.get('custom_params', [])]) if config.get('custom_params') else "None"}

      ### Instructions for the Target LLM:
      - Do not generate an answer to the base prompt.
      - Instead, produce a prompt template that instructs the user’s desired response.
      - Your output should clearly outline how the final answer must be structured, including tone, style, step-by-step instructions, and any other details as specified.
      - The final prompt should be clear, engaging, and fully aligned with the user preferences provided above.

      End of prompt.
"""
    
    # Build the system message for the assistant.
    assistant_sys_msg = BaseMessage.make_assistant_message(
        role_name='Assistant',
        content="You are an expert prompt engineer with over 10 years of experience crafting detailed prompt templates for LLMs.",
    )
    
    # Create the ChatAgent using the global model instance.
    agent = ChatAgent(assistant_sys_msg, model=MODEL_INSTANCE, token_limit=4096)
    
    # Send the detailed_prompt as the user message.
    user_msg = BaseMessage.make_user_message(
        role_name="User",
        content=detailed_prompt
    )
    
    # Call the LLM service and extract the content.
    assistant_response = agent.step(user_msg).msg.content
    logger.debug(f"LLM RESPONSE: {assistant_response}")
    print(f"LLM RESPONSE: ----> {assistant_response}")
    
    # Prepare log details for debugging.
    log_details = {
        "Base Prompt": config.get('base_prompt', ''),
        "Personality": config.get('personality', ''),
        "Creativity": config.get('creativity', ''),
        "Output Format": config.get('output_format', ''),
        "Response Length": config.get('response_length', '')
    }
    if 'custom_params' in config:
        log_details["Custom Parameters"] = config['custom_params']
    
    print("Script executed successfully")
    return assistant_response, log_details


