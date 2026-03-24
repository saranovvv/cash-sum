import tkinter as tk
# from log.mainlog import log_frame


class main_frame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="red", width=100, height=100)
        self.pack()



