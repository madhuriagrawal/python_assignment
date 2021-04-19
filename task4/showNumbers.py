def showNumbers(limit):
    for i in range(limit):
        if i%2==0:
            print(i,"EVEN")
        else:
            print(i, "ODD")

showNumbers(4)