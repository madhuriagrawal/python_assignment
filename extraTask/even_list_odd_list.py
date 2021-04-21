import functools
def even_list_old_list():
    even_list=[]
    odd_list=[]
    while len(even_list)+len(odd_list)<10:

        number=int(input("Enter a number between 1 to 50:"))

        if number%2==0 :
            if len(even_list)<5:

                even_list.append(number)
        else:
            if len(odd_list)<5:

                odd_list.append(number)


    resEven=functools.reduce(lambda a,b:a+b, even_list)
    resOdd=functools.reduce(lambda a,b:a+b, odd_list)
    print(resOdd ,resEven)
    return max(resOdd,resEven)

print(even_list_old_list())
