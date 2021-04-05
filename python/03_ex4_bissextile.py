annee = int(input("Entrez une année: "))

if (annee%100==0 and annee%400==0):
    print("l'année "+str(annee)+" est bissextile")
elif (annee%100==0):
     print("l'année "+str(annee)+" n'est pas bissextile")
elif (annee%4==0):
    print("l'année "+str(annee)+" est bissextile")
else: 
    print("l'année "+str(annee)+" n'est pas bissextile")