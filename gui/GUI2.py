import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 40, window=entry1)


def get_square_root():
    x1 = entry1.get()

    label1 = tk.Label(root, text=x1)
    canvas1.create_window(200, 230, window=label1)


button1 = tk.Button(text='Please provide scenario name', command=get_square_root)
canvas1.create_window(200, 80, window=button1)

root.mainloop()