import numpy as np
import matplotlib.pyplot as plt

# définition de l'intervalle de l'axe des abscisses
x = np.linspace(0, 10, 100)
# la ou les fonction...
y = 2*(x**3) - 3*(x**2) + 5
#y1 = 2*x + 10
#y2 = 3*x


# limiter les bornes d'affichage selon les axes :
plt.xlim(0, 10)
#plt.ylim(0, 800)

# Insérer des sous-titres aux axes :
plt.xlabel("axe des abscisses")
plt.ylabel("axe des ordonnées")

# Insérer un titre :
plt.title("Titre")

# Afficher la grille :
plt.grid()

# Afficher la courbe :
# On peut changer la couleur d’une courbe en intégrant comme argument à la fonction 
# plot() un des caractères suivants : « r » pour la couleur rouge, « y » pour la couleur jaune, 
# « k » pour la couleur noire, « g » pour la couleur verte, « w » pour la couleur blanche,
#  « b » pour la couleur bleu, « m » pour la couleur magenta, « c » pour la couleur cyan.
# et Insérer une légende :
plt.plot(x, y, label = "2x**3 -3x**2 + 5")
#plt.plot(x, y1, 'y', label="y1 = 2*x + 10")
#plt.plot(x, y2, 'r', label="y2 = 3*x")
# on lance le rendu, avec ou sans personnalisation des options pour la légende...
#plt.legend(loc='upper center', shadow=True, fontsize='x-large')
plt.legend()
plt.show()

# pour plus d'options et aller plus loin : cf tuto et documentation de matplotlib...