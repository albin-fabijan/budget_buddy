import tkinter as tk

class DisplayWindow1440x1024(tk.Tk):
    def __init__(self):
        WINDOW_WIDTH = 1440
        WINDOW_HEIGHT = 1024

    def main(self):
        self.creat_window()

    def creat_window(self):
        main_window = tk.Tk()
        main_window.title("Menu")
        main_window.geometry("1100x700")
        main_window.resizable(0, 0)
        main_window.config(background="#FFFFFF")
        icon = tk.PhotoImage(file='budget_buddy/images/acajou_accounts.png')
        main_window.iconphoto(True, icon)
        main_window.mainloop()


