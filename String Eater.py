string = "Hallo, ik ben een string en ik word opgegeten."

class string_length:
    length = len(string)

def eat():
    if string_length.length > 0:
        def eater():
            print(string[:string_length.length])
            string_length.length -= 1
            eat()
        eater()
    else:
        exit()

# def eat():
    # length = len(string)

    # while length > 0:
        # print(string[:length])
        # length -= 1

eat()