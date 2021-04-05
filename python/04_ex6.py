chaine=str(input("Entrez une chaîne de caractères: "))

inverse=""
for i in range (len(chaine),0,-1):
    inverse+=chaine[i-1]

print(inverse)

# en vrai on aurait pu faire simplement print(chaine[::-1]) mais on fait de l'algo...