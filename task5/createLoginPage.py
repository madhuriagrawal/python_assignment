usename=input("Enter username: ")
password=input("Enter password: ")
Re_Password=input("Enter password again: ")

counter=1

while counter<=2:
    if password != Re_Password:
        print("oops! passwords didn't match")
        password = input("Enter password: ")
        Re_Password=input("Enter password again: ")
        counter+=1
    else:
        print("you are logged in!")
        break

