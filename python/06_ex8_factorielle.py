def factorielle(n):
    if n==1:
        return n
    else:
        return n*factorielle(n-1)

nombre=int(input("Entrez un entier: "))
print("La factorielle de",nombre,"est",factorielle(nombre))