x=123

i = 0

count = 0
for i in x:
    print(i)
#it will give the error :'int' object is not iterable


while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")
# output will be
# 0
# error
# 1
# error
# 2

while True:
    print(count)
    count += 1
    if count >= 5:
        break

#output will be
# 0
# 1
# 2
# 3
# 4
