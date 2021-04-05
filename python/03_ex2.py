nombre1 = int(input("Entrez un premier nombre: "))
nombre2 = int(input("Entrez un deuxième nombre: "))

if (nombre1<=nombre2):
    produit10=nombre1*10
    if (nombre2>produit10):
        print("Le deuxième nombre est strictement supérieur à 10 fois le premier")
else:
    produit10=nombre2*10
    if (nombre1>produit10):
        print("Le premier nombre est strictement supérieur à 10 fois le deuxième")

print("fin du programme")
