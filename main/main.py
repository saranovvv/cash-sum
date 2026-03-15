import tkinter as tk
import top.top as header
import ms.main_site as mains
import ss.sum as sums

root = tk.Tk()
root.title("Cash&Sum by saranov")
root.geometry("1000x500")

# top frame
top_frame = header.topframe(root,1000,100,"red")
top_frame.place()

# main site
main_site = mains.main_site(root, 800, 400, "green")
main_site.place()

sum_site = sums.sum_frame(root, 200, 400, "blue")
sum_site.place()


root.mainloop()