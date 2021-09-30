string = "Hallo, ik ben een string en ik word opgegeten."

def eat():
    length = len(string)
    
    while length > 0:
        print(string[:length])
        length -= 1

eat()