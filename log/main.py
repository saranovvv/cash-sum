from imp import *
import log_frame as lf
import top_log_frame as tlf
class log():
    title = "Zaloguj się do serwisu"
    
    
    def __init__(self):
        pass


    def centerwindow(self, root, width, height):
        self.root = root
        self.width = width
        self.height = height
        
        screen_height = self.root.winfo_screenheight()
        screen_width = self.root.winfo_screenwidth()

        x = (screen_width/2) - (self.width/2)
        y = (screen_height/2) - (self.height/2)

        self.root.geometry('%dx%d+%d+%d' % (self.width, screen_height, x, y))

    def startwindow(self):
        root = tk.Tk()
        root.title(self.title)
        root.attributes("-topmost", True)
        self.centerwindow(root, 1000, 1000)
        
        top_frame = tlf.top_log_frame()
        top_frame.place(root, 1000, 100)

        log_frame = lf.log_frame()
        log_frame.place(root)

        root.mainloop()

if __name__ == "__main__":
    root = log()
    root.startwindow()
    
    
    