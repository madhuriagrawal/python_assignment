x=input("enter one option from Addition, Subtraction, Division, Multiplication, Average:")
if x=="Average":
    num1,num2,num3,num4=input("Enter four numbers: ").split()
else:
    num1,num2=input("Enter two numbers: ").split()


if x=="Addition":
    sum=int(num1)+int(num2)
    if sum>0:
        print(sum)
    else:
        print("NEGATIVE")

elif x == "Subtraction":
    sub = int(num1) - int(num2)
    if sub > 0:
        print(sub)
    else:
        print("NEGATIVE")

elif x == "Division":
    div = int(num1) / int(num2)
    if div > 0:
        print(div)
    else:
        print("NEGATIVE")

elif x == "Multiplication":
    mul = int(num1) * int(num2)
    if mul > 0:
        print(mul)
    else:
        print("NEGATIVE")

elif x == "Average":
    avg = (int(num1) + int(num2)+int(num3)+int(num4))/4
    if avg > 0:
        print(avg)
    else:
        print("NEGATIVE")


