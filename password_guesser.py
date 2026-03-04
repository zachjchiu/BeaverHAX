password = "Andre_is_a_bum."
user_guess = input ("Please enter the password: ")
while user_guess != password:
    print("Incorrect password.")
    print("Here's a hint: it has 4 words seperated by _. the  first starts with A. This sentence ends in a .")
    print("The words are 5, 2, 1, and 3 letters long, respectively.")
    user_guess = input ("Please enter the password: ")