nombre1 = int(input("Entrez un premier nombre: "))
nombre2 = int(input("Entrez un deuxième nombre: "))

if (nombre1<=nombre2):
    if (nombre2%nombre1==0):
        print("le nombre "+str(nombre2)+" est un multiple de "+str(nombre1))
    else:
        print("le nombre "+str(nombre2)+" n'est pas un multiple de "+str(nombre1))
else:
    if (nombre1%nombre2==0):
        print("le nombre "+str(nombre1)+" est un multiple de "+str(nombre2))
    else:
        print("le nombre "+str(nombre1)+" n'est pas un multiple de "+str(nombre2))

