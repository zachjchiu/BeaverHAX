
score = input("Enter your test score: ")
if int(score) <= 100 and int(score) >= 94:
    print("You got an A.")
elif int(score) <= 93 and int(score) >= 85:
    print("You got an B.")
elif int(score) <= 84 and int(score) >= 78:
    print("You got a C.")
elif int(score) <= 78 and int(score) >= 65:
    print("You got a D.")
elif int(score) <= 64:
    print("You got an F. You are a bum. You are a failure that failed.")
else:
    print("You cheated. Your a super bum. I'm going to email your parents and teachers.")
    print("Email sending.")
    print("Email sent.")


grades = {"math": 100, "english": 95, "bvr hax": 70}
user_input = input("Enter a subject to see your grade: ")
if user_input == "math":
    print("Your grade in math is: " + str(grades["math"]))
elif user_input == "english":
    print("Your grade in english is: " + str(grades["english"]))
elif user_input == "bvr hax":
    print("Your grade in bvr hax is: " + str(grades["bvr hax"]))
else:    
    print("You don't have a grade in that subject. You are a failure that failed.") 

andre_grades = {"math": 0, "english": 8, "bvr hax": 1}
andre2_grades = andre_grades
andre3_grades = andre2_grades
andre3_grades["english"] = 4
print(andre_grades)
print(andre2_grades)
print(andre3_grades)

fruits = ["apples", "grapes", "banana"]
evil_fruits = fruits
evil_fruits.extend(["durian", "dragonfruit"])
tropical_fruits = evil_fruits
tropical_fruits.extend(["mango"])
tropical_fruits.extend(["papaya"])
print(fruits)