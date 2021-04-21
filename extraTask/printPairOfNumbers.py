
def printPairOfNumbers(x,resultNumber):
    for i in range(len(x)-1):
        for j in range(i+1,len(x)):
            if x[i]+x[j]==resultNumber:
                print(x[i],x[j])






resultNumber = 8
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1]
printPairOfNumbers(x,resultNumber)