def swapingUsingThirdVariable():
    x=2
    y=6
    z=x
    x=y
    y=z
    print(x,y)
def swapingWithoutThirdVariable():
    x = 2
    y = 6
    x,y=y,x

    print(x,y)

swapingUsingThirdVariable()
swapingWithoutThirdVariable()

