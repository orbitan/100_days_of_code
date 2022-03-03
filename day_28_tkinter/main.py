from tkinter import *

pad_y = 10

window = Tk()
window.title("My First GUI Program")
window.minsize(width=800, height=500)


def sel():
    number = int(amount.get())
    if v.get() == 1:
        res = str(number * 1.609) + " kilometers"
    else:
        res = str((number / 1.609)) + " miles"
    text = Label(text=res).pack(pady=pad_y)


v = IntVar()

wn_heading = Label(text="Converter", font=("Arial", 25)).pack(pady=pad_y)
amount = Entry()
amount.pack(pady=pad_y)
convert = Button(text="Convert").pack(pady=pad_y)

miles = Radiobutton(text="Miles", variable=v, value=1, command=sel)
miles.pack()
kilometers = Radiobutton(text="Kilometers", variable=v, value=2, command=sel)
kilometers.pack()

window.mainloop()
