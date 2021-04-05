import os as os
import itertools as it

def test():

    print("Hello")
    #répertoire du dico
   # os.chdir("C:/Users/Etu/Desktop/IPI/reseau/ShellIAUX081/IAUX081")

    dico = open("dict_fr_gutenberg", "r", encoding="utf-8")
    print(dico)
    mot = str(input("Mettre 7 ou 8 lettres : "))
    print(mot)
    while len(mot) != 7 and len(mot) != 8:
        mot = str(input("Mettre 7 ou 8 lettres : "))


    possibilite = it.permutations(mot, len(mot))

    for line in dico:
        mdico = line.strip()
        for possi in possibilite:
            if possi.__eq__(mdico):
                print("le mot existe")
                exit(0)

    print("le mot n'existe pas")
    exit(1)

test()
