import tkinter as tk
import log.frames.log_frame as lf
import log.frames.top_log_frame as tlf


# zrobić to na tk.Frame
# bez tego .tkraise() nie bedzie dzialal 

class log_frame(tk.Frame):  
    def __init__(self, master):
        super().__init__(master)
        self.config(bg="green", width=150, height=150)
        self.pack()