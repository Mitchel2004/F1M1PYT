string = "Hallo, ik ben een string en ik word opgegeten."

class the_length:
    length = len(string)

def eat():
    if the_length.length > 0:
        def eating():
            print(string[:the_length.length])
            the_length.length -= 1
            eat()
        
        eating()
    else:
        exit()

# def eat():
    # length = len(string)
    
    # while length > 0:
        # print(string[:length])
        # length -= 1

eat()