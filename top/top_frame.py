import tkinter as tk
from main import start

class top_frame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="green")
        self.grid(row=0, column=0, columnspan=10, rowspan=2, sticky=tk.NSEW)
        log_butt(self)

class log_butt(tk.Button):
    def __init__(self, master):
        super().__init__(master)
        self.config(text="Logowanie", command=lambda: start.change_frame())
        self.pack()
       
                 