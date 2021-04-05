def prime(n):
    for i in range(2,n):
        if (n%i==0):
            print("le nombre",n,"n'est pas premier, il est divisible par",i)
            return True
    print("le nombre",n,"est un nombre premier (il n'est divisible que par 2 nombres distincts: 1 et lui même)")
        


nombre=int(input("Entrez un nombre: "))

prime(nombre)