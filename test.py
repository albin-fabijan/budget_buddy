import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def plot_graph1():
    # Données à afficher pour le premier graphique
    x1 = [1, 2, 3, 4, 5]
    y1 = [2, -3, 5, 7, 11]

    # Création du premier graphique
    fig1, ax1 = plt.subplots()
    ax1.plot(x1, y1, marker='o')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_title('Graphique 1')

    # Intégration du premier graphique dans tkinter
    canvas1 = FigureCanvasTkAgg(fig1, master=frame1)
    canvas1.draw()
    canvas1.get_tk_widget().pack()

def plot_graph2():
    # Données à afficher pour le deuxième graphique
    x2 = [1, 2, 3, 4, 5]
    y2 = [3, 4, 2, 6, 8]

    # Création du deuxième graphique
    fig2, ax2 = plt.subplots()
    ax2.plot(x2, y2, marker='o')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_title('Graphique 2')

    # Intégration du deuxième graphique dans tkinter
    canvas2 = FigureCanvasTkAgg(fig2, master=frame2)
    canvas2.draw()
    canvas2.get_tk_widget().pack()

# Création de la fenêtre tkinter
root = tk.Tk()
root.title("Graphiques avec tkinter")

# Création du cadre bleu
frame1 = tk.Frame(root)
frame1.pack(side=tk.LEFT)

frame2 = tk.Frame(root, bg="blue")
frame2.pack(side=tk.LEFT)

# Affichage des graphiques dans les cadres correspondants
plot_graph1()
plot_graph2()

# Boucle principale tkinter
root.mainloop()
