nblignes=int(input("veuillez saisir le nombre de lignes de vos matrices: "))
nbcolonnes=int(input("veuillez saisir le nombre de colonnes de vos matrices: "))

a=range(nblignes)  
b=range(nbcolonnes) 

matrice1=[[0 for i in b] for j in a]
matrice2=[[0 for i in b] for j in a]


print("saisie de la matrice 1")
for i in range (0,nblignes):
    print("saisie de la ligne",i+1)
    for j in range (0,nbcolonnes):
        matrice1[i][j]=int(input("Saisissez la valeur de la colonne "+str(j+1)+" pour la ligne "+str(i+1)+": "))


print("saisie de la matrice 2")
for i in range (0,nblignes):
    print("saisie de la ligne",i+1)
    for j in range (0,nbcolonnes):
        matrice2[i][j]=int(input("Saisissez la valeur de la colonne "+str(j+1)+" pour la ligne "+str(i+1)+": "))

addition=[[matrice1[i][j]+matrice2[i][j] for j in range(nbcolonnes)] for i in range (nblignes)]


print("Matrice 1")
for i in range (0,len(matrice1)):
    print(matrice1[i])

print("Matrice 2")
for i in range (0,len(matrice2)):
    print(matrice2[i])

print("Matrice 1 + Matrice 2")
for i in range (0,len(addition)):
    print(addition[i])