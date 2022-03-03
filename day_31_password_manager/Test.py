from tkinter import *

from PIL import ImageTk, Image

root = Tk()
root.geometry("600x400")

canvas = Canvas(root, width=300, height=400)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("logo.png"))

canvas.create_image(20, 20, anchor=NW, image=img)
root.mainloop()