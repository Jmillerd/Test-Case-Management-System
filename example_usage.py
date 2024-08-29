# example_usage.py

from test_case_generator import TestCaseGenerator

# Instantiate and generate a test case
generator = TestCaseGenerator(model_name='gpt2')
prompt = "messages"
generated_test_case = generator.generate_test_case_components(prompt)
print(generated_test_case)
