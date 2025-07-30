import requests
from Task2.user import User
from Task2.data_manager import DataManager

def create_test_user_data():
    return {
        "name": "Kanishkasree",
        "email": "kaniskasree804@gmail.com",
        "password": "Pass@123",
        "age": 20,
        "role": "intern"
    }

def safe_web_request(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.exceptions.MissingSchema:
        print("Invalid URL format.")
    except requests.exceptions.ConnectionError:
        print("Connection error occurred.")
    except requests.exceptions.Timeout:
        print("Request timed out.")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    return None


if __name__ == "__main__":
    print("Creating a test user dictionary: ")
    user_data = create_test_user_data()
    print("Test User Data:", user_data)

    print("\nGenerating a random user: ")
    random_user = User.generate_random_user()
    print("Random User:")
    print("Name:", random_user.name)
    print("Email:", random_user.email)
    print("Password:", random_user.password)
    print("Is Valid Email?", random_user.is_valid())

    print("\nLoading users from 'sample.json':")
    data_manager = DataManager("sample.json")
    users = data_manager.load_test_users()

    print("\nChecking if users are valid: ")

    index = 1  

    for user in users:
       print("User", index)
       print("Name:", user.name)
       print("Email:", user.email)
       print("Password:", user.password)
       print("Is Valid Email?", user.is_valid())
       print("-----------------------------")
       index += 1


    print("\nSaving validation results to 'results.json': ")
    results = []

    for user in users:
        result = {
            "name": user.name,
            "email": user.email,
            "valid": user.is_valid()
        }
        results.append(result)

    data_manager.save_test_results(results, "results.json")

    
    print("\nMaking a safe web request to 'https://www.google.com': ")
    html = safe_web_request("https://www.google.com")

    if html is not None:
        print("Request successful!")
        print("First 100 characters of the page:")
        print(html[:100])
    else:
        print("Web request failed.")

