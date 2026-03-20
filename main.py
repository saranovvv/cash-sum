import tkinter as tk
import time
# import subprocess

from log.mainlog import *

class start():
    title = "Cash&Sum by srv"
    def __init__(self):
        pass

    def log(self, main_frame, root):
        main_frame.pack_forget()
        logowanie = log()
        logowanie.startlog(root)

    def test(self):
        print("test")

    def startwindow(self):
        root = tk.Tk()
        root.geometry("500x500")

        main_frame = tk.Frame(root, width=20, height=10)
        main_frame.pack()

        b1 = tk.Button(main_frame, text="Logowanie", command=lambda : self.log(main_frame, root))
        b1.pack()




        root.mainloop()

if __name__ == "__main__":
    root = start()
    root.startwindow()
    