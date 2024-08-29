from test_case_generator import TestCaseGenerator
import testrail_client


class TestCaseIntegration:
    def __init__(self, model_name, project_id, section_id):
        self.generator = TestCaseGenerator(model_name)
        self.project_id = project_id
        self.section_id = section_id

    def generate_prompt(self, feature_name):
        return f"Generate test cases for the {feature_name} feature."

    def integrate_with_testrail(self, feature_name):
        title, automation_type, preconditions, steps, expected_results = self.generator.generate_test_case_components(feature_name)
        
        response = self.client.add_case(title, automation_type, preconditions, steps, expected_results, self.project_id, self.section_id)
        return response

# Example usage
integration = TestCaseIntegration(
    model_name='gpt2',
    project_id=1,  # Replace with your project ID
    section_id=1   # Replace with your test section ID
)

feature_name = "Login"  # Replace with your feature name
response = integration.integrate_with_testrail(feature_name)
print("TestRail Response:", response)
