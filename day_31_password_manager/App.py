from tkinter import *
from PIL import ImageTk, Image

from day_31_password_manager.Controller import Controller
from day_31_password_manager.Model import Model
from day_31_password_manager.View import View


class App:
    def __init__(self):

        model = Model("Stupid")

        view = View()
        controller = Controller(model, view)
        view.set_controller(controller)
        view.root.mainloop()


if __name__ == "__main__":
    app = App()
