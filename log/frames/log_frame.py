import tkinter as tk

class log_frame():
    def __init__(self):
        pass

    def place(self, root):
        self.root = root
        frame = tk.Frame(self.root, bg="red", width=100, height=100)
        frame.grid(row=1, column=0)
        

    def test(self):
        pass