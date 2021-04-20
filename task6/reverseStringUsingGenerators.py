def reverseString(InputString):
    length = len(InputString)
    for i in range(length - 1, -1, -1):

        yield InputString[i]

for char in reverseString("Consultadd Training"):
    print(char)

