def max(liste):
    maximum=liste[0]
    for i in range (1,len(liste)):
        if liste[i]>maximum:
            maximum=liste[i]
    return maximum

        
liste=[]
print("Maximum d'une liste")
i=input("Entrez la première valeur de la liste: ")
while i!="":
    liste.append(float(i))
    i=input("Entrez la valeur suivante (vide pour terminer): ")


print("Le maximum de cette liste est",max(liste))


