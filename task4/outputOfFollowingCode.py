def foo():
try:
    return 1
finally:
    return 2
k = foo()
print(k)

# it will give indentation error because try block is not inside the function foo()



def a():
try:
    f(x, 4)
finally:
    print('after f')
    print('after f?')
a()

# it will give indentation error because try block is not inside the function a()
