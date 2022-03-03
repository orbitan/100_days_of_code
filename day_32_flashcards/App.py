import time

import pandas

from day_32_flashcards.Controller import Controller
from day_32_flashcards.Model import Model
from day_32_flashcards.ViewFlashCard import View


class App:
    def __init__(self):

        model = Model("Stupid")
        self.view = View()
        controller = Controller(model, self.view)
        self.view.set_controller(controller)
        self.view.root.mainloop()


if __name__ == "__main__":
    app = App()





