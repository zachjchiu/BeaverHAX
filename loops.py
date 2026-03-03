print("Sign up sequence activated.")
username = input("Enter a username: ")
password = input("Enter a password: ")
logged_in = False
while logged_in == False:
    for i in range(10):
        print(i)
    numbers = []
    stop = False
    while stop == False:
        numberadd = input("Enter a number or 'stop': ")
        if numberadd == "stop":
            stop = True
            continue
        numbers.append(int(numberadd))
    print(numbers)

    for number in numbers:
        if number > 50:
            print(number)
        else:
            continue
    print("These are the numbers above 50.")

    number = 100
    while (number > 10):
        number = (number + 10) / 3
        print(number)

    print("Initiating startup.")
    log_in_username = input("Enter your username: ")
    log_in_password = input("Enter your password: ")
    if log_in_username == username and log_in_password == password:
        print("You are now logged in.")
        logged_in = True
        continue
    else:
        print("Incorrect username or password. Please try again.")
print("Welcome to the program.")
