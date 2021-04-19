import functools
x=functools.reduce(lambda a,b:str(a)+str(b), [1,2,3,4,5,6,7])
print(x)