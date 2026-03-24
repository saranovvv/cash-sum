import tkinter as tk
# from log.mainlog import log_frame


class main_frame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="red")
        self.grid(row=2, column=0, columnspan=7, rowspan=8, sticky=tk.NSEW)