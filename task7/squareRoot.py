import math


class squareRoot:

    def findSquareRoot(self,C,H,*D):
        for i in D:
            print(math.sqrt((2*C*i)/H))



x=squareRoot()
x.findSquareRoot(50,30,1,2,3,4,5,6,)