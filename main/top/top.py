import tkinter as tk

class topframe:
    def __init__(self, root, width, height, color):
        self.root   = root
        self.height = height
        self.width = width
        self.color = color


    def place(self):
        global frame
        frame = tk.Frame(self.root, height=self.height, width=self.width, bg=str(self.color))
        frame.grid(row=0, column=0, columnspan=2, sticky="N")        


   
     