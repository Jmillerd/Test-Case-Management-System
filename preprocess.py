import pandas as pd

# Load the CSV file
df = pd.read_csv('data/test_case_data.csv')

# Display the first few rows of the dataframe
print(df.head())

def clean_text(text):
    # Example text cleaning function
    if pd.isna(text):
        return ""
    return text.strip().replace('\n', ' ').replace('\r', '')

df['Title'] = df['Title'].apply(clean_text)
df['Priority'] = df['Priority'].apply(clean_text)

# Define the structure for the JSON data
structured_data = df[['Title','Priority', 'Automation Type', 'Section']].to_dict(orient='records')

# Optionally, save to a JSON file
import json

with open('test_cases.json', 'w') as json_file:
    json.dump(structured_data, json_file, indent=4)

# Display a sample of the structured data
print(structured_data[:2])


# Load JSON file for validation
with open('test_cases.json', 'r') as json_file:
    json_data = json.load(json_file)

# Check the first few entries
for item in json_data[:2]:
    print(item)

