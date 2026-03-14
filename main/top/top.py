import tkinter as tk

class test:
    def __init__(self, root,width, height, color):
        self.root   = root
        self.width = width
        self.height = height
        self.color = color


    def place(self):
        global frame
        frame = tk.Frame(self.root,width=self.width, height=self.height, bg=str(self.color))
        frame.pack()
        
   
     