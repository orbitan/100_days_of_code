import time
import tkinter
from tkinter import *
from PIL import ImageTk, Image

BACKGROUND_COLOR = "#b3d8d5"
CARD_FRONT_IMAGE = "images/card_front.png"
CARD_BACK_IMAGE = "images/card_back.png"
UNKNOWN_BUTTON = "images/wrong.png"
KNOWN_BUTTON = "images/right.png"


class View:

    def __init__(self):
        self.root = Tk()
        self.controller = None
        self.title = self.root.title("Flashcard App")
        self.root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        self.status = False
        self.flip = 0
        self.front_card = tkinter.PhotoImage(file=CARD_FRONT_IMAGE)
        self.back_card = tkinter.PhotoImage(file=CARD_BACK_IMAGE)

        self.canvas = Canvas(self.root, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.grid(column=0, row=0, columnspan=2)
        self.image_container = self.canvas.create_image(400, 263, image=self.front_card)

        self.language = self.canvas.create_text(400, 150, text="Dutch", font=('Helvetica', '40', 'italic'))
        self.answer = self.canvas.create_text(400, 300, text="zijn", font=('Helvetica', '50', 'bold'))

        self.known_button = tkinter.PhotoImage(file=KNOWN_BUTTON)
        self.unknown_button = tkinter.PhotoImage(file=UNKNOWN_BUTTON)

        self.k_button = Button(self.root, image=self.known_button, command=self.button_clicked)
        self.k_button.grid(column=0, row=1)

        self.u_button = Button(self.root, image=self.unknown_button, command=self.button_clicked)
        self.u_button.grid(column=1, row=1)

        self.canvas.after(3000, self.flip_card)


    def set_controller(self, controller):
        self.controller = controller

    def next_card(self):
        if self.controller:
            new_question = self.controller.get_next_word()
            self.canvas.itemconfig(self.answer, text=new_question)

    def flip_card(self):
        self.flip += 1
        if self.controller:
            if self.status is True:
                self.canvas.itemconfig(self.image_container, image=self.front_card)
                self.canvas.itemconfig(self.language, text="Dutch", fill="black")
                self.canvas.itemconfig(self.answer, text="switch")
                self.next_card()
                self.status = False
                self.canvas.after(3000, self.flip_card)
            else:
                translation = self.controller.get_translation()
                self.canvas.itemconfig(self.image_container, image=self.back_card)
                self.canvas.itemconfig(self.language, text="English", fill="black")
                self.canvas.itemconfig(self.answer, text=translation, fill="black")

                self.status = True


    def button_clicked(self):
        if self.flip > 1:
            self.controller.add_to_known_words()
        self.flip_card()
        #  self.next_card()







