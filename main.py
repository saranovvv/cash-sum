import tkinter as tk
from log.mainlog import *
from mainfr.main_frame import *
from top.top_frame import *

class start():
    title = "Cash&Sum by srv"
    def __init__(self):
        pass

    def centerwindow(self, root, width, height):
        root.update_idletasks()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        root.geometry(f"{width}x{height}+{x}+{y}")

    

    def startwindow(self):
        root = tk.Tk()
        self.centerwindow(root, 1000, 800)

        mf = main_frame(root)
        lf = log_frame(root)


        self.index = 0
        self.framelist = [mf, lf]
        self.framelist[1].forget()

        tk.Button(root, text="logowanie", command=self.button).pack()

        root.mainloop()

    def button(self):
        self.framelist[self.index].forget()
        self.index = (self.index + 1) % len(self.framelist)
        self.framelist[self.index].tkraise()
        self.framelist[self.index].pack()


if __name__ == "__main__":
    root = start()
    root.startwindow()
    