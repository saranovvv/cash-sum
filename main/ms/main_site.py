import tkinter as tk

class main_site:
    def __init__(self, root, width, height, color):
        self.root = root
        self.height = height 
        self.width = width
        self.color = color

    def place(self):
        ms = tk.Frame(self.root, height=self.height, width=self.width, bg=str(self.color))
        ms.grid(row=1, column=0, sticky="W")
