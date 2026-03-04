def password_game():
    print("Welcome to the Password Game by Zachary Chiu.")
    rule_1 = False
    rule_2 = False 
    rule_3 = False
    rule_4 = False
    rule_5 = False
    password = input("Please choose a password: ")
    check = True
    while check == True:
        while rule_1 == False:
            for i in range(10):
                if str(i) in password:
                    rule_1 = True
                    break
                else:
                    continue
            if rule_1 == True:
                break
            else:
                print("❌ Rule 1: Include at lease one number in your password.")
                rule_1 = False
                password = input("Please choose a password: ")
            for i in range(10):
                if str(i) in password:
                    rule_1 = True
                    break
                else:
                    continue
            if rule_1 == True:
                break
            else:
                print("❌ Rule 1: Include at lease one number in your password.")
                rule_1 = False
                password = input("Please choose a password: ")
        while rule_2 == False and rule_1 == True:
            if any(x.isupper() for x in password):
                rule_2 = True
            else:
                print("❌ Rule 2: Include at least one uppercase letter in your password.")
                rule_2 = False
                password = input("Please choose a password: ")
            rule_1 = False
            rule_2 = False 
            rule_3 = False
            rule_4 = False
            rule_5 = False
            for i in range(10):
                if str(i) in password:
                    rule_1 = True
                    break
                else:
                    continue
            if rule_1 == True:
                break
            else:
                print("❌ Rule 1: Include at lease one number in your password.")
                rule_1 = False
                password = input("Please choose a password: ")
            if any(x.isupper() for x in password):
                rule_2 = True
            else:
                print("❌ Rule 2: Include at least one uppercase letter in your password.")
                rule_2 = False
                password = input("Please choose a password: ")
        while rule_3 == False and rule_2 == True and rule_1 == True:
            if any(x.islower() for x in password):
                rule_3 = True
            else:
                print("❌ Rule 3: Include at least one lowercase letter in your password.")
                rule_3 = False
                password = input("Please choose a password: ")
            rule_1 = False
            rule_2 = False 
            rule_3 = False
            rule_4 = False
            rule_5 = False
            for i in range(10):
                if str(i) in password:
                    rule_1 = True
                    break
                else:
                    continue
            if rule_1 == True:
                break
            else:
                print("❌ Rule 1: Include at lease one number in your password.")
                rule_1 = False
                password = input("Please choose a password: ")
            if any(x.isupper() for x in password):
                rule_2 = True
            else:
                print("❌ Rule 2: Include at least one uppercase letter in your password.")
                rule_2 = False
                password = input("Please choose a password: ")
            if any(x.islower() for x in password):
                rule_3 = True
            else:
                print("❌ Rule 3: Include at least one lowercase letter in your password.")
                rule_3 = False
                password = input("Please choose a password: ")
        while rule_4 == False and rule_3 == True and rule_2 == True and rule_1 == True:
            if any(x in "!@#$%^&*()-_=+[]{}|;:,.<>?/~`" for x in password):
                rule_4 = True
            else:
                print("❌ Rule 4: Include at least one special character in your password.")
                rule_4 = False
                password = input("Please choose a password: ")
            rule_1 = False
            rule_2 = False 
            rule_3 = False
            rule_4 = False
            rule_5 = False
            for i in range(10):
                if str(i) in password:
                    rule_1 = True
                    break
                else:
                    continue
            if rule_1 == True:
                break
            else:
                print("❌ Rule 1: Include at lease one number in your password.")
                rule_1 = False
                password = input("Please choose a password: ")
            if any(x.isupper() for x in password):
                rule_2 = True
            else:
                print("❌ Rule 2: Include at least one uppercase letter in your password.")
                rule_2 = False
                password = input("Please choose a password: ")
            if any(x.islower() for x in password):
                rule_3 = True
            else:
                print("❌ Rule 3: Include at least one lowercase letter in your password.")
                rule_3 = False
                password = input("Please choose a password: ")
            if any(x in "!@#$%^&*()-_=+[]{}|;:,.<>?/~`" for x in password):
                rule_4 = True
            else:
                print("❌ Rule 4: Include at least one special character in your password.")
                rule_4 = False
                password = input("Please choose a password: ")
        while rule_5 == False and rule_4 == True and rule_3 == True and rule_2 == True and rule_1 == True:
            if len(password) >= 8:
                rule_5 = True
            else:
                print("❌ Rule 5: Your password must be at least 8 characters long.")
                rule_5 = False
                password = input("Please choose a password: ")
            rule_1 = False
            rule_2 = False 
            rule_3 = False
            rule_4 = False
            rule_5 = False
            for i in range(10):
                if str(i) in password:
                    rule_1 = True
                    break
                else:
                    continue
            if rule_1 == True:
                break
            else:
                print("❌ Rule 1: Include at lease one number in your password.")
                rule_1 = False
                password = input("Please choose a password: ")
            if any(x.isupper() for x in password):
                rule_2 = True
            else:
                print("❌ Rule 2: Include at least one uppercase letter in your password.")
                rule_2 = False
                password = input("Please choose a password: ")
            if any(x.islower() for x in password):
                rule_3 = True
            else:
                print("❌ Rule 3: Include at least one lowercase letter in your password.")
                rule_3 = False
                password = input("Please choose a password: ")
            if any(x in "!@#$%^&*()-_=+[]{}|;:,.<>?/~`" for x in password):
                rule_4 = True
            else:
                print("❌ Rule 4: Include at least one special character in your password.")
                rule_4 = False
                password = input("Please choose a password: ")
            if len(password) >= 8:
                rule_5 = True
            else:
                print("❌ Rule 5: Your password must be at least 8 characters long.")
                rule_5 = False
                password = input("Please choose a password: ")
password_game()