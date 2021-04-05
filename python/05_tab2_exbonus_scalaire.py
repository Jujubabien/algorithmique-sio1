# on saisit les dimensions de la matrice
nblignes=int(input("veuillez saisir le nombre de lignes de vos matrices: "))
nbcolonnes=int(input("veuillez saisir le nombre de colonnes de vos matrices: "))
multiplicateur=int(input("veuillez saisir le nombre par lequel multiplier la matrice: "))

a=range(nblignes)  
b=range(nbcolonnes) 
matrice=[[0 for i in b] for j in a]
resultat=[[0 for i in b] for j in a]


# on saisit la matrice
# pour chaque ligne
for i in range (0,nblignes):
    print("saisie de la ligne",i+1)
    # pour chaque colonne
    for j in range (0,nbcolonnes):
        # je saisit la valeur de l'élément d'indice i j soit Matrice(i j)
        matrice[i][j]=int(input("Saisissez la valeur de la colonne "+str(j+1)+" pour la ligne "+str(i+1)+": "))


# traitement/calcul : produit scalaire
# pour chaque ligne
# pour chaque colonne
# resultat(i j) = scalaire * matrice (i j)
for i in a:
    # pour chaque pour colonne
    for j in b:
       resultat[i][j]=multiplicateur*matrice[i][j]


# on affiche la matrice
print("Matrice")
for i in range (0,len(matrice)):
    print(matrice[i])
# on affiche le résultat
print("Résultat")
for i in range (0,len(matrice)):
    print(resultat[i])