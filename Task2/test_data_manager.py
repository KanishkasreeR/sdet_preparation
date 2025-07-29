import json
from test_user import TestUser
from functions import read_test_data_from_json

class TestDataManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_test_users(self):
        data = read_test_data_from_json(self.file_path)
        users = []

        if data:
            for user in data:
                name = user['name']
                email = user['email']
                password = user['password']

                new_user = TestUser(name, email, password)
                users.append(new_user)

        return users

    def save_test_results(self, results, output_file):
        try:
            with open(output_file, 'w') as file:
                json.dump(results, file, indent=4)
            print(f"Results saved to '{output_file}'.")
        except Exception:
            print("Something went wrong while saving the results.")

