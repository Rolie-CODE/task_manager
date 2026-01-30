from menu import main_menu,sign_up_menu
while True:
    main_menu()
    sign_up_menu()
    request = input("")
    try:
        request = int(request)
    except ValueError:
        print(f"{request} is not a valid input")

    if request == 1:
        pass

    elif request == 2:
        pass

    elif request == 3:
        pass

    else:
        print(f"{request} is not a valid input")
    
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
