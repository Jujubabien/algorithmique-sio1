def pgcd(n1,n2):
    if (n1<n2):
        nb1=n1
        nb2=n2
    else:
        nb1=n2
        nb2=n1

    reste=1
    while nb2!=0:
        reste=nb1%nb2
        nb1,nb2=nb2,reste
        #nb1=nb2
        #nb2=reste
    return nb1

def pgcd_recursif(n1,n2):
    if (n2==0):
        return n1
    else:
        return pgcd(n2,n1%n2)
        

print("Calcul du PGCD de deux nombres")
nombre1=int(input("Entrez le nombre 1: "))
nombre2=int(input("Entrez le nombre 2: "))

if (pgcd(nombre1,nombre2)==1):
    print(nombre1,"et",nombre2,"sont premiers entre eux")
else:
    print("le PGCD de ",nombre1,"et",nombre2,"est",pgcd(nombre1,nombre2))

if (nombre1<nombre2):
    nb1=nombre1
    nb2=nombre2
else:
    nb1=nombre2
    nb2=nombre1

if (pgcd_recursif(nb1,nb2)==1):
    print(nb1,"et",nb2,"sont premiers entre eux")
else:
    print("le PGCD de ",nb1,"et",nb2,"est",pgcd_recursif(nb1,nb2))
