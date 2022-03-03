import math
import time
from tkinter import *
import random

PIXEL_WIDTH = 5
TOTAL_PIXEL = 82 * 82
WIDTH = 82
HEIGHT = 82
X_1 = []


class View(Frame):
    def __init__(self, parent):
        super().__init__(parent)


        #  Widgets
        self.break_button = Button(self, text="Break", width=5, height=1, command=self.break_button_clicked)
        self.break_button.place(x=0, y=0)

        self.break_button = Button(self, text="Work", width=5, height=1, command=self.break_button_clicked)
        self.break_button.pack(padx=10, pady=10)

        self.task_var = StringVar()
        self.task_entry = Entry(self, textvariable=self.task_var, width=30)
        self.task_entry.pack(padx=10, pady=10)

        self.submit_button = Button(self, text="Submit", command=self.submit)
        self.submit_button.pack()

        self.message_label = Label(self, text='', foreground='red')

        #  Controller
        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

    def show_success(self, message):
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.pack()
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.task_entry['foreground'] = 'black'
        self.task_var.set('')

    def hide_message(self):
        self.message_label['text'] = ''

    def submit(self):
        if self.controller:
            self.controller.save(self.task_var.get())

        self.show_success("Successfull")

    def break_button_clicked(self):
        canvas = Canvas(height=400, width=400, bg="#d8b3b3")
        canvas.place(x=0, y=0)

        work = Button(text="Work", command=self.work_button_clicked)
        work.pack()


        pixel_to_rect = lambda x, y: [x * PIXEL_WIDTH, y * PIXEL_WIDTH, x * PIXEL_WIDTH + PIXEL_WIDTH,
                                      y * PIXEL_WIDTH + PIXEL_WIDTH]
        pixels = [(x, y) for y in range(HEIGHT) for x in range(WIDTH)]
        random.shuffle(pixels)

        for pixel in pixels:
            canvas.create_rectangle(*pixel_to_rect(*pixel), fill="green", tags="rect", outline="")
            self.update()
        canvas.destroy()

    def work_button_clicked(self):
        time.sleep(5)
        canvas = Canvas(height=400, width=400, bg="red")
        canvas.place(x=0, y=0)

        break_button = Button(text="Break", command=self.break_button_clicked)
        break_button.pack()


        pixel_to_rect = lambda x, y: [x * PIXEL_WIDTH, y * PIXEL_WIDTH, x * PIXEL_WIDTH + PIXEL_WIDTH,
                                      y * PIXEL_WIDTH + PIXEL_WIDTH]
        pixels = [(x, y) for y in range(HEIGHT) for x in range(WIDTH)]
        random.shuffle(pixels)

        for pixel in pixels:
            canvas.create_rectangle(*pixel_to_rect(*pixel), fill="green", tags="rect", outline="")
            self.update()
        canvas.destroy()
