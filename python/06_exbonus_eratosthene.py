def eratosthene(n):
    crible = list(range(n + 1))                  # <0,...,n>, 0 n'est pas premier
    crible[1] = 0                                # 1 n'est pas premier

    i = 2                                   # Entier à tester
    while i**2 <= n:                        # Inutile de tester jusqu'à n
        if crible[i] != 0:                       # Si i n'est pas étiqueté (=0)...
        # ...étiqueter tous les multiples de i: de 2 * i à n (inclu) par pas de i
            for j in range(2 * i, n + 1, i):
             crible[j] = 0
        i += 1                              # Passer à l'entier à tester suivant

           
    return crible

        


nombre=int(input("Entrez un nombre: "))

print("Voici les nombres premiers jusqu'à",nombre)
print([i for i in eratosthene(nombre) if i != 0])