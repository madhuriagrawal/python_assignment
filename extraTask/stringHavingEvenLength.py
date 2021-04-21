inputString="hello my name is abcde"
tmp=inputString.split()
print(tmp)
for i in tmp:

    if len(i)%2==0:
        print(i)