import json
from accounts import user_accounts

def save_data(user_accounts):
    with open('accounts.json', 'w') as file:
        json.dump(user_accounts, file, indent=4)

def load_data():
    try:
        with open('accounts.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}