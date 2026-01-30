user_accounts = {
    "Username": {
        "password": "password",
        "tasks": []
    }
}

def register(user_accounts, username, password):
    if username in user_accounts:
        print("Username already exists")
    else:
        user_accounts[username] = {
            "password": password,
            "tasks": []
        }
        print("User registered successfully")

def login(username, password):
    if username in user_accounts:
        if user_accounts[username]["password"] == password:
            print("Login successful")
            return True
    print("Invalid username or password")
    return False