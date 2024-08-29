from transformers import GPT2LMHeadModel, GPT2Tokenizer

import re

class TestCaseGenerator:
    def __init__(self, model_name):
        # Load the model and tokenizer
        self.model = self.load_model(model_name)
        self.tokenizer = self.load_tokenizer(model_name)
        
    def load_model(self, model_name):
        # Implement model loading logic
        pass
        
    def load_tokenizer(self, model_name):
        # Implement tokenizer loading logic
        pass
    
    def generate_test_case_components(self, feature_name):
        prompt = f"Generate a detailed test case for the {feature_name} feature. Include title, preconditions, steps, and expected results. Format as: Title: [Feature Name] - Test Case, Preconditions: [List of conditions], Steps: [Numbered list], Expected Results: [Description]."
        inputs = self.tokenizer(prompt, return_tensors='pt', padding=True)
        outputs = self.model.generate(**inputs, do_sample=True, temperature=0.7)
        
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Post-process the generated text
        title, preconditions, steps, expected_results = self.process_generated_text(generated_text)
        return title, preconditions, steps, expected_results
    
    def process_generated_text(self, text):
        # Initialize default values
        title = ""
        preconditions = ""
        steps = ""
        expected_results = ""
        
        # Split the text into sections
        sections = re.split(r'\n(?=\d+\.)', text)  # Split on numbered steps
        
        if len(sections) >= 4:
            # Extract the title
            title_section = sections[0]
            title_match = re.search(r'^Title:\s*(.*)', title_section, re.MULTILINE)
            if title_match:
                title = title_match.group(1).strip()
            
            # Extract the preconditions
            preconditions_section = sections[1]
            preconditions_match = re.search(r'^Preconditions:\s*(.*)', preconditions_section, re.MULTILINE)
            if preconditions_match:
                preconditions = preconditions_match.group(1).strip()
            
            # Extract the steps
            steps_section = sections[2]
            steps_match = re.search(r'^Steps:\s*(.*)', steps_section, re.MULTILINE)
            if steps_match:
                steps = steps_match.group(1).strip()
                # Ensure steps are numbered
                steps = self.format_numbered_list(steps)
            
            # Extract the expected results
            expected_results_section = sections[3]
            expected_results_match = re.search(r'^Expected Results:\s*(.*)', expected_results_section, re.MULTILINE)
            if expected_results_match:
                expected_results = expected_results_match.group(1).strip()
        
        return title, preconditions, steps, expected_results
    
    def format_numbered_list(self, text):
        # Format steps as a numbered list
        steps = re.split(r'(\d+\.)', text)
        formatted_steps = ""
        for i in range(1, len(steps), 2):
            if i + 1 < len(steps):
                formatted_steps += f"{steps[i].strip()} {steps[i+1].strip()}\n"
        return formatted_steps.strip()

