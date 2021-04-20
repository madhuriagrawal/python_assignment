students = ['Smit', 'Jaya', 'Rayyan']
subjects = ['CSE', 'Networking', 'Operating System']
res={k:v for k,v in zip(students,subjects)}
print("dictionary using dictionary comprehension: ")
print(res)


#using for loop
res={}
for k,v in zip(students,subjects):
    res[k]=v
print("dictionary using for loop: ")
print(res)
