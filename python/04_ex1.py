
print("nombres entiers de 7 à 23")
for i in range (7,24):
    print(i,end=" ")
print("")

print("nombres pairs <100")

i=0
while i<100:
    if (i%2==0):
        print(i,end=" ")
    i+=1

# on fait de l'algo donc c'est acceptable. En vrai, un programmeur aurait fait : 
# i=0
# while (i<100):
#    print(i,end=" ")
#    i+=2
# ce qui aurait optimisé la boucle : 2 fois moins d'itérations et un if/test de condition en moins à chaque itération...


print("")

print("nombres impairs compris entre 2 et 28")

i=3
while i<29:
    print(i,end=" ")
    i+=2
print("")

print("nombres multiples de 3 compris entre 5 et 32")

i=5
while i<32:
    if (i%3==0):
        print(i,end=" ")
    i+=1

print("")
# optimisation
# i=6
# while i<32:
#     print(i,end=" ")
#     i+=3
# 3 fois moins d'itérations, un calcul et un test en moins à chaque itération...

print("Jours de la semaine")
# pour rappel, on a pas encore vu les tableaux/listes/dictionnaires...
i=0
while i<7:
    if i==0:
        print("Lundi",end=" ")
    elif i==1:
        print("Mardi",end=" ")
    elif i==2:
        print("Mercredi",end=" ")
    elif i==3:
        print("Jeudi",end=" ")
    elif i==4:
        print("Vendredi",end=" ")
    elif i==5:
        print("Samedi",end=" ")
    elif i==6:
        print("Dimanche",end=" ")
    i+=1
print("")