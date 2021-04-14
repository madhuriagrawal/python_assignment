x=input("enter a input")
digits = sum(i.isdigit() for i in x)
letters = sum(i.isalpha() for i in x)

print("letters are ",letters)
print("digits are ",digits)
