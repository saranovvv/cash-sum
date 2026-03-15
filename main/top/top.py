import tkinter as tk

class topframe:
    def __init__(self, root, width, height, color):
        self.root = root
        self.height = height
        self.width = width
        self.color = color
    
    def place(self):
        global frame
        frame = tk.Frame(self.root, height=self.height, width=self.width, bg=str(self.color))
        frame.grid(row=0, column=0, columnspan=2)

    def opcje(self):
        global opcje_frame
        opcje_frame = tk.Frame(frame, height=self.height, width=self.height, bg="pink")
        opcje_frame.place(x=0, y=0)

    def test(self):
        test = tk.Label(frame, text="test")
        test.place(x=500, y=0)
   

     