import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

def select_date():
    # Fonction appelée lorsque le bouton est cliqué
    def on_date_selected():
        selected_date.set(cal.get_date())
        top.destroy()  # Fermer la fenêtre après la sélection de la date

    # Créer une fenêtre pop-up pour afficher le calendrier
    top = tk.Toplevel(root)

    # Créer un objet Calendar
    cal = Calendar(top, selectmode='day', date_pattern='yyyy-mm-dd')

    # Bouton pour sélectionner la date
    select_button = ttk.Button(top, text="Sélectionner", command=on_date_selected)
    select_button.pack(pady=10)

    # Afficher le calendrier
    cal.pack()

# Créer la fenêtre principale
root = tk.Tk()
root.title("Sélecteur de date")

# Variable pour stocker la date sélectionnée
selected_date = tk.StringVar()

# Champ de texte pour afficher la date sélectionnée
date_label = ttk.Label(root, textvariable=selected_date)
date_label.pack(pady=10)

# Bouton pour ouvrir le sélecteur de date
select_button = ttk.Button(root, text="Ouvrir le sélecteur de date", command=select_date)
select_button.pack(pady=10)

# Lancer la boucle principale
root.mainloop()
