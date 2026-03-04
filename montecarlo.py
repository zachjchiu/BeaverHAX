import random
import math
inside_circle_count = 0
total_count = 0
number_of_times = input("How many times do you want to run the Monte-Carlo simulation? ")
for i in range(int(number_of_times)):
        x = random.uniform(0, 2)
        y = random.uniform(0, 2)
        coordinates = [x, y]
        center = [1, 1]
        distance = math.dist(coordinates, center)
        if distance <= 1:
            inside_circle_count = inside_circle_count + 1 
        if i%(int(number_of_times)/100) == 0:
            print(f"Run {i} times, {(i/int(number_of_times))*100}% complete")
        total_count = total_count + 1
pi = (inside_circle_count/total_count)*4
print("\n")
print("Pi is about " + str(pi))