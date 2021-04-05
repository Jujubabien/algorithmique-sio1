nblignes=int(input("veuillez saisir le nombre de lignes de votre matrice: "))
nbcolonnes=int(input("veuillez saisir le nombre de colonnes de votre matrice: "))

a=range(nblignes)  
b=range(nbcolonnes) 

matrice=[[0 for i in b] for j in a]
transpose=[[0 for i in a] for j in b]

# saisie de la matrice
for i in a:
    print("saisie de la ligne",i+1)
    for j in b:
        matrice[i][j]=int(input("Saisissez la valeur de la colonne "+str(j+1)+" pour la ligne "+str(i+1)+": "))


for i in a:
    for j in b:
        transpose[j][i] = matrice[i][j]


print("Matrice")
for i in a:
    print(matrice[i])

print("Transposée")
for i in b:
    print(transpose[i])