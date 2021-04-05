nblignes=int(input("veuillez saisir le nombre de lignes de votre matrice: "))
nbcolonnes=int(input("veuillez saisir le nombre de colonnes de votre matrice: "))

a=range(nblignes)  
b=range(nbcolonnes) 
print(a)

matrice=[[0 for i in b] for j in a]

# saisie de la matrice
for i in a:
    print("saisie de la ligne",i+1)
    for j in b:
        matrice[i][j]=int(input("Saisissez la valeur de la colonne "+str(j+1)+" pour la ligne "+str(i+1)+": "))


transpose=[[matrice[j][i] for j in a] for i in b]


print("Matrice")
for i in range (0,len(matrice)):
    print(matrice[i])

print("Transposée")
for i in range (0,len(transpose)):
    print(transpose[i])