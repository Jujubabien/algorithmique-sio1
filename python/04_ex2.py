nombre = int(input("Entrez un nombre: "))

print("table de multiplication de "+str(nombre))
for i in range (0,11):
    print(i,"x",nombre,"=",i*nombre)