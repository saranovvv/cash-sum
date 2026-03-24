import tkinter as tk


class log_frame(tk.Frame):  
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="white")
        self.grid(row=2, column=0, columnspan=10, rowspan=8, sticky=tk.NSEW)