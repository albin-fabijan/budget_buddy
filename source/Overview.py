import tkinter as tk
from tkinter import ttk
from Header import Header

WINDOW_WIDTH = 1440
WINDOW_HEIGHT = 1024

main_window = tk.Tk()

main_window.title("Test")
main_window.geometry("1100x700")
main_window.resizable(0, 0)
main_window.title('Test')
main_window.config(background="#FFFFFF")

header = Header()
header.run(main_window)

main_window.mainloop()