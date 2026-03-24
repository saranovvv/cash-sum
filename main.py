import tkinter as tk
from top.top_frame import *
from mainfr.main_frame import *
from sum.sum_frame import *
from log.log_frame import *





class start(tk.Tk):
    def __init__(self):
        super().__init__()

        self.centerwindow(1000, 800)
        self.startwindow()

        self.mainloop()
    
    def startwindow(self):
        for i in range(10):
            self.grid_columnconfigure(i, weight=1)
            self.grid_rowconfigure(i, weight=1)

        self.framelist = [top_frame(self), main_frame(self), sum_frame(self), log_frame(self)]
        self.framelist[3].grid_forget()


    def centerwindow(self, width, height):
        self.update_idletasks()
        self.title("Cash-Sum by saranov")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.geometry(f"{width}x{height}+{x}+{y}")


if __name__ == "__main__":
    try:
        start()
    except:
        print(AttributeError)