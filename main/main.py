import tkinter as tk
import top.top as header
import ms.main_site as ms

root = tk.Tk()
root.title("Cash&Sum by saranov")
root.geometry("1000x500")

top_frame = header.test(root,1000, 50, "red")
top_frame.place()

main_site = ms.main_site()

root.mainloop()