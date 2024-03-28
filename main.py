import tkinter as tk
from tkinter import ttk
from source.filteredsearchview import filteredsearchview
from source.filterpopup import filterpopup

WINDOW_WIDTH = 1440
WINDOW_HEIGHT = 1024

def create_window() :
    main_window = tk.Tk()

    main_window.title("Menu")
    main_window.geometry("1100x700")
    main_window.resizable(0, 0)
    main_window.config(background="#FFFFFF")
    icon = tk.PhotoImage(file='budget_buddy/images/acajou_accounts.png')
    main_window.iconphoto(True, icon)

    menu = filteredsearchview()
    menu.main(main_window, "Djibril", "Mimouni")
    

    main_window.mainloop()

create_window()