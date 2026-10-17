#Project_3
for i in range(5):
    print(i)
developer = 'Devin'

print(type(developer))
count = 1

print("Done!")

# Part 3: The Random Number Game
import random

secret_number = random.randint(1, 10)
print("I've picked a number between 1 and 10. Try to guess it!")

while True:
    # 1. Ask for their guess inside the loop (remember to convert to an int!)
    user_guess = int(input("Number: "))
    
    # 2. Check the guess
    if user_guess == secret_number:
        print("You won!")
        break  # What keyword stops the loop?
    elif user_guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")  # Print that it's too high!


#Challenge_1
grade = int(input("Enter your grade: ")) 
if grade>= 90:
    letter_grade = "A"
elif grade>= 80:
    letter_grade = "B"
elif grade>= 70:
    letter_grade = "C"
elif grade>= 50:
    letter_grade = "D"
else:
    letter_grade = "F"
print("Your letter grade is " + letter_grade)
#Challenge_2
print("Enter 2 numbers, It will divide them and give you the remainder.")
Number_1 = float(input("Number1: "))
Number_2 = float(input("Number2: "))
Remainder = Number_1 % Number_2
print("Remainder: " + str(Remainder))
#Challenge_3
Name = input("What's your name? ")
Favorite_Game = input("What's your favorite game? ")
print ("That's a great name, " + Name + " I enjoy playing " + Favorite_Game + " As well!")
