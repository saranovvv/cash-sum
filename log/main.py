from imp import *

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

        self.root.attributes("-topmost", True)
        root.geometry('%dx%d+%d+%d' % (self.width, screen_height, x, y))

    def startwindow(self):
        root = tk.Tk()
        root.title(self.title)
        self.centerwindow(root, 1000, 1000)

        root.mainloop()

if __name__ == "__main__":
    root = log()
    root.startwindow()