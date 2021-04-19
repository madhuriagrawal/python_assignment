s="abcSdefPghijQkl"
countUpper=0
countLower=0
for i in s:
    if i.isupper():
        countUpper+=1
    elif i.islower():
        countLower+=1
print("number of uppercases is: ",countUpper)
print("number of lowercases is:", countLower)