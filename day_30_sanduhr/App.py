from tkinter import *

from day_30_sanduhr.Controller import Controller
from day_30_sanduhr.Model import Model
from day_30_sanduhr.View import View


class App(Tk):
    def __init__(self, master=None):
        super().__init__()
        self.geometry("400x400")
        self.title("Study Timer")
        model = Model("Stupid")

        view = View(self)
        view.pack()

        controller = Controller(model, view)

        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
