class sumToZero:
    def findSumToZero(self,realNumbers):

        output=[]


        for i in range(len(realNumbers)-2):
            for j in range(i+1,len(realNumbers)-1):
                for k in range(j+1,len(realNumbers)):
                    myList = []
                    if realNumbers[i]+realNumbers[j]+realNumbers[k]==0:
                        myList=[realNumbers[i],realNumbers[j],realNumbers[k]]
                        output.append(myList)

        print(output)

x=sumToZero()
realNumbers=[-25,-10,-7,-3,2,4,8,10]
x.findSumToZero(realNumbers)