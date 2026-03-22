import tkinter as tk
# from log.mainlog import log_frame
import os
print(os.getcwd())


class chfrbut():
    def __init__(self, master):
        self.root = master

        button = tk.Button(self.root, text="logowanie", command=self.logowanie)
        button.pack()

    def logowanie(self):
        print("test")


class main_frame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="red", width=100, height=100)
        self.pack()

