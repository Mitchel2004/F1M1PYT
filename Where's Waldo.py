import random

people = ["Waldo", "Jackson", "Ray", "Eric", "Vaughn", "Jesse", "Herbert", "Robert", "Rodrigo", "Elija", "Sasha", "Nathaniel", "Ellie", "Allison", "Jeremiah", "Paula", "Alisha", "Tory", "Troy", "Faye"]
random.shuffle(people)

print("Lijst:")

num = 0

for p in people:
    num += 1
    
    if len(str(num)) == 1:
        print(str(num) + ".  " + p, sep="\n")
    else:
        print(str(num) + ". " + p, sep="\n")

for w in people:
    if w == "Waldo":
        if people.index(w) == 0:
            print("\nWaldo is op plaats 1.")
        else:
            print("\nWaldo is op plaats " + str(people.index(w) + 1) + ".")