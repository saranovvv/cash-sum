import tkinter as tk
import top.top as header
import ms.main_site as mains
import ss.sum as sums

root = tk.Tk()
root.title("Cash&Sum by saranov")
root.geometry("1000x500")
root.update_idletasks()


tk.Grid.rowconfigure(root, 0, weight = 1)
tk.Grid.columnconfigure(root, 0, weight = 1)



top_frame = header.topframe(root,root.winfo_width(),100,"red")
top_frame.place()
top_frame.opcje()
top_frame.test()

main_site = mains.main_site(root, 800, 400, "green")
main_site.place()





sum_site = sums.sum_frame(root, 200, 400, "blue")
sum_site.place()

root.mainloop()