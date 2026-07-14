cities = ["Addis Ababa","Adama","Hawassa","Bahir Dar"]
cities [0]
cities [-1]
cities [1:3]
len (cities)
cities.append ("Harrer")
cities.remove ("Harrer")


totals = []
for p in [100,200,250]:
    totals.append (p*0.15)


names = ["almaz","kebede","ayele"]
for names in names:
    print (f"Good Morning, {names}")


names = ["almaz","kebede","ayele"]
for i, names in enumerate (names, 1):
    print (f"{i}.{names}")


country = ("Ethiopia","Ertria")
famous , nighbour = country
country [0]= "asmera" 

a=(1,2,3)
b=(4,5,6)
print (a|b)