import tkinter as tk
class top_log_frame():
    def __init__(self):
        pass

    def place(self, root, width, height):
        self.root = root
        self.width = width
        self.height = height

        top_log_frame = tk.Frame(self.root, bg="green", width=self.width, height=self.height)
        top_log_frame.grid(row=0, column=0, sticky=tk.NSEW)