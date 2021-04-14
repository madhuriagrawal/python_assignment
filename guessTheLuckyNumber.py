import random

number=input("guess the lucky number")
correctNumber=random.randint(0,9)
while True:
    if int(number)==correctNumber:
        break
    else:
        answer=input("Do you want to guess again? yes or no")
        if answer=="yes":
            number = input("guess the lucky number")

        else:
            break



