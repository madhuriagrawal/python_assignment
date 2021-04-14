
import random

number = input("guess the lucky number")
correctNumber=random.randint(0,9)
counter = 1
while counter <= 5:

    if int(number) == correctNumber:
        print("Good Guess!")

    elif counter == 5:
        print("Game Over!")
        break
    else:
        print("try again!")
        counter = counter + 1
        number = input("guess the lucky number")

