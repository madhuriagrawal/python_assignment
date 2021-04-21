stringInput="12abcbacbaba344ab"
myDict={}
for i in stringInput:
    if i>='a' and i<='z':
        if i in myDict:
            myDict[i]=myDict[i]+1
        else:
            myDict[i]=1

for k,v in myDict.items():
    print(k,"=",v)