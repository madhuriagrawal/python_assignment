l=[1,2,4,5,7,8,9,5,77,9,21]
x=list(filter(lambda a:a%3!=0 and a%7==0, l ))
print(x)