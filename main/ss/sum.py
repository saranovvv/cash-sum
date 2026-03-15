import tkinter as tk

class sum_frame:
    def __init__(self, root, width, height, color):
        self.root = root
        self.width = width
        self.height = height
        self.color = color
    
    def place(self):
        sums = tk.Frame(self.root, width=self.width, height=self.height, bg=str(self.color))
        sums.grid(row=1, column=1, sticky="E")