import json

def validate_email_format(email):
    return "@" in email and "." in email

def read_test_data_from_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except json.JSONDecodeError:
        print("Error: File is not a valid JSON.")
    return None