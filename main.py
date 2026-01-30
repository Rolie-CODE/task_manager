from menu import main_menu,sign_up_menu
from accounts import user_accounts, register, login
from storage import save_data, load_data

user_accounts = load_data()

while True:    
    sign_up_menu()
    request = input("")
    try:
        request = int(request)

    except ValueError:
        print(f"{request} is not a valid input")
        continue

    if request == 1:
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        confirm_password = input("Confirm your password: ").strip()
        if password == confirm_password:
            register(user_accounts, username, password)
            save_data(user_accounts)
        else:
            print("Passwords do not match")

    elif request == 2:
        username = input("Enter your username: ").strip()
        password = input("Enter your password: ").strip()
        if login(username, password):
            print("Login successful!")
            save_data(user_accounts)
        else:
            print("Login failed.")
        break

    elif request == 3:
        print("Thank you for using the Royal Task Manager!")
        break

    else:
        print(f"{request} is not a valid input")
        break

    main_menu()
    request = input("")

    try:
        request = int(request)

    except ValueError:
        print("Please enter a valid number.")
        continue

    if request == 1:
        pass

    elif request == 2:
        pass

    elif request == 3:
        pass

    elif request == 4:
        pass

    else:
        print(f"{request} is an invalid input")
        break
