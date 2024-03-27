import matplotlib.pyplot as plt

# Créer des données de test
x = [1, 2, 3, 4, 5]
y = [10, 15, 13, 18, 16]

# Créer une nouvelle figure avec la taille spécifiée
plt.figure(figsize=(13.15, 5.81))

# Tracer les données
plt.plot(x, y)

# Ajouter des étiquettes et un titre
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Titre du graphique')

# Afficher le graphique
plt.show()