inputString="nvfguffjjghhguoa"
x=inputString[::-1]
print(x)
for i in range(len(x)):
    if x[i]=="a" or x[i]=="e" or x[i]=="i" or x[i]=="o" or x[i]=="u":
        print("index=",i,"alphabet=",x[i])
