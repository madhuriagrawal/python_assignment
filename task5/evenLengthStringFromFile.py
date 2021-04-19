with open('doc.txt', 'r') as file:

    for line in file:
        for word in line.split():
            if len(word)%2==0:
                print(word)