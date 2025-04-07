export const usePromptValidator = () => {
    const validate = (prompt: string, selectedPersonality: string) => {
      const errors: string[] = [];
      
      // Basic validation
      if (prompt.length < 20) errors.push("Prompt too short (min 20 characters)");
      if (prompt.length > 2000) errors.push("Prompt too long (max 2000 characters)");
      
      // Content validation
      const requiredSections = ['Base Instruction', 'Persona'];
      requiredSections.forEach(section => {
        if (!prompt.includes(section)) errors.push(`Missing ${section} section`);
      });
  
      // Personality-specific rules
      if (selectedPersonality === 'Academic' && !prompt.includes('Citations')) {
        errors.push("Academic prompts require citation sources");
      }
  
      return {
        isValid: errors.length === 0,
        errors
      };
    };
  
    return { validate };
  };