a= eval(input("Enter hyphen separated words:"))
input=a.split("-")
input.sort()
s="-"
s=s.join(input)
print(s)
