import tkinter as tk

class sum_frame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="blue")
        self.grid(row=2, column=7, columnspan=3, rowspan=8, sticky=tk.NSEW)