import tkinter as tk
from tkinter import ttk
from source.Overview import Overview
from source.NotificationPage import NotificationPage

class Window :
    def create_window(self) :
        main_window = tk.Tk()

        main_window.title("Menu")
        main_window.geometry("1100x700")
        main_window.resizable(0, 0)
        main_window.config(background="#FFFFFF")
        icon = tk.PhotoImage(file='budget_buddy/images/acajou_accounts.png')
        main_window.iconphoto(True, icon)

        menu = Overview()
        menu.run(main_window, "Djibril", "Mimouni")

        main_window.mainloop()