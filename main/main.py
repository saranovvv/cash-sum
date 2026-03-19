from imp import *

class start():
    title = "Cash&Sum by srv"
    def __init__(self):
        pass

    def log(self):
        subprocess.run(["python3", "../log/main.py"])
    def test(self):
        print("test")
    def startwindow(self):
        root = tk.Tk()
        root.geometry("500x500")
        tk.Button(root, text="Zaloguj się", command=self.log).pack()
        tk.Button(root, text="test", command=self.test).pack()
        
        root.mainloop()

if __name__ == "__main__":
    root = start()
    root.startwindow()
    