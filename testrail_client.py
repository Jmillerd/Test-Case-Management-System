import base64
import json

import requests

from api_client import APIClient


client = APIClient('https://....testrail.io/')
client.user = ''
client.password = ''
      

# Retrieve Case Data functions

def get_case(case_id):
    case = client.send_get('get_case/{}'.format(case_id))
    print(case)

def get_cases(project_id, suite_id):
    cases = client.send_get('get_cases/{}&suite_id={}'.format(project_id, suite_id))
    print(cases)

def get_case_fields(self):
    case_fields = client.send_get('get_case_fields')
    print(case_fields)

def get_templates(project_id):
    templates = client.send_get('get_templates/{}'.format(project_id))
    print(templates)

def get_priorities(self):
    priorities = client.send_get(get_priorities)
    print(priorities)

def get_case_types(self):
    case_types = client.send_get('get_case_types')
    print(case_types)

def get_case_statuses(self):
    case_statuses = client.send_get('get_case_statuses')
    print(case_statuses)

# Case Creation and Manipulation Functions

def add_case(self, title, automation_type, preconditions, steps, expected_results, project_id, section_id):
        payload = {
            'title': title,
            'type_id': 1,  # Ensure this maps to the correct type ID
            'priority_id': 1,  # You can modify this if needed
            'estimate': '3m',  # Modify or remove if not required
            'refs': '',  # Add references if needed
            'custom_preconds': preconditions,
            'custom_steps': steps,
            'custom_expected': expected_results,
            'project_id': project_id,
        }
        added_case = client.send_post('add_case/{}'.format(section_id),payload) 
        print(added_case)

def copy_cases_to_section(section_id):
    copied_cases = client.send_post('copy_cases_to_section/{}'.format(section_id))
    print(copied_cases)

def moved_cases_to_section(section_id):
    moved_cases = client.send_post('copy_cases_to_section/{}'.format(section_id))
    print(moved_cases)

def update_case(case_id):
    updated_case = client.send_post('update_case/{case_id}'.format(case_id))
    print(updated_case)

def update_cases(section_id):
    updated_cases = client.send_post('update_case/{case_id}'.format(section_id))
    print(updated_cases)

def delete_case(case_id):
    deleted_case = client.send_post('delete_case/{case_id}'.format(case_id))
    print(deleted_case)

def delete_cases(suite_id):
    deleted_cases = client.send_post('delete_cases/{suite_id}'.format(suite_id))
    print(deleted_cases)


