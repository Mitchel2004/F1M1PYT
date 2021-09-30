from os import system, name
import time
import re

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

item = "Laptop"

factory = []
distribution = []
shop = []

def text():
    print("Factory     : " + str(*factory))
    print("Distribution: " + str(*distribution))
    print("Shop        : " + str(*shop))

def transport():
    def eind():
        clear()
        text()
        print("Nog een keer? J/N")
        jn = input()
        jnup = jn.upper()
            
        if re.match("^[JNjn]*$", jnup):
            if jnup == "J":
                clear()
                transport()
            elif jnup == "N":
                clear()
                exit()
        else:
            print("Typ alleen de letters J of N!")
            time.sleep(3)
            eind()
    
    text()
    time.sleep(1)
    factory.insert(0, item)
    clear()
    text()
    time.sleep(1)
    factory.pop(0)
    distribution.insert(0, item)
    clear()
    text()
    time.sleep(1)
    distribution.pop(0)
    shop.insert(0, item)
    clear()
    text()
    time.sleep(1)
    shop.pop(0)
    clear()
    text()
    time.sleep(1)
    eind()

transport()