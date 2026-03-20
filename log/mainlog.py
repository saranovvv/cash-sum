import tkinter as tk
import log.frames.log_frame as lf
import log.frames.top_log_frame as tlf
class log():    

    def __init__(self):
        pass

    def startlog(self, root):
        top_frame = tlf.top_log_frame()
        top_frame.place(root, 100, 100)
        pass
        


    # def centerwindow(self, root, width, height):
    #     self.root = root
    #     self.width = width
    #     self.height = height
        
    #     screen_height = self.root.winfo_screenheight()
    #     screen_width = self.root.winfo_screenwidth()

    #     x = (screen_width/2) - (self.width/2)
    #     y = (screen_height/2) - (self.height/2)

    #     self.root.geometry('%dx%d+%d+%d' % (self.width, screen_height, x, y))
