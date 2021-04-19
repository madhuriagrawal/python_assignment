def findWordWithMaxLength(a,b):
    if len(a)>len(b):
        print(a)
    elif len(a)==len(b):
        print(a)
        print(b)

    else:
        print(b)

a=input("enter a string:")
b=input("enter another string:")
findWordWithMaxLength(a,b)