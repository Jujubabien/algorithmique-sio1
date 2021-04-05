def nboccurences(liste,cherche):
    nb=0
    for i in range (0,len(liste)):
        if liste[i]==float(cherche):
            nb+=1
    return nb

        
liste=[]
print("nombre d'occurences d'un nombre dans une liste")
i=input("Entrez la première valeur de la liste: ")
while i!="":
    liste.append(float(i))
    i=input("Entrez la valeur suivante (vide pour terminer): ")

nombre=input("Entrez la valeur à rechercher dans la liste: ")



print("Le nombre d'occurences de",nombre,"dans la liste est",nboccurences(liste,nombre))


