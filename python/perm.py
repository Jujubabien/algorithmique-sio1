#!/usr/bin/pypy

from itertools import permutations

# saisie des lettres au clavier
lettres = input("Entrez les lettres : ")

# ouverture/fermeture du fichier liste de mots pour constitution d'une liste python de mots  
ficlistemot=open("dict_fr_gutenberg","r")
# dictionnaire alternatif possible
#ficlistemot=open("/usr/share/dict/french","r")
dictionnaire=ficlistemot.read().splitlines()
ficlistemot.close()

# initialisation d'un dictionnaire de résultats
resultat={}

# algo/traitement : pour toutes les longueur possibles sur l'itérable lettres (itertools/permutations)  de longeur 3 à longueur de lettres, on obtient 
# toutes les permutations possibles pour la longueur donnée. Pour chaque élément des permutations, on "assemble/convertit en chaîne" (join) le mot à 
# partir de l'élément de permutation et s'il n'est pas déjà dans les résultat trouvés (cas des doublons constatés si des lettres sont en double dans 
# les lettres entrées) on vérifie si la permutation actuelle est un mot faisant partie du "dictionnaire" : si oui, on le rajoute au résultat
for i in range(3,len(lettres)+1):
         for subset in permutations(lettres,i):
            mot="".join(subset)
            if mot not in resultat:
                if mot in dictionnaire:
                 resultat[mot]=mot

# affichage des résultats
long=2
for i in resultat:
    if long<len(i):
        long=len(i)
        print("mots de",long,"lettres")
    print(i)
