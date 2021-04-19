try:
    number = input("Enter 4 digit number: ")
    if len(number)>4:
        raise ValueError("The length is too short/long !!! Please provide only four digits")
except ValueError as ve:
    print(ve)