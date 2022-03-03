import random
import string
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

LOWER_LETTERS = list(string.ascii_lowercase)
UPPER_LETTERS = list(string.ascii_uppercase)
SPECIAL_CASES = ["!", "*", "-"]
CHOOSE_LIST = [LOWER_LETTERS, UPPER_LETTERS, [i for i in range(0, 9)], SPECIAL_CASES]


class View:

    def __init__(self):
        self.root = Tk()
        self.title = self.root.title("Password Manager")
        self.root.config(padx=100, pady=50)

        self.set_photo()
        self.set_labels()

        self.controller = None

    def set_photo(self):
        self.canvas = Canvas(self.root, width=200, height=200)
        self.photo = ImageTk.PhotoImage(Image.open("logo.png"))
        self.canvas.create_image(100, 100, image=self.photo)
        self.canvas.grid(column=1, row=0)

    def set_labels(self):
        self.label_website = Label(text="Website:").grid(column=0, row=1)
        self.label_email = Label(text="Email/Username:").grid(column=0, row=2)
        self.label_password = Label(text="Password:").grid(column=0, row=3)
        self.entry_website = Entry(width=35)
        self.entry_website.grid(column=1, row=1, columnspan=2)
        self.entry_email = Entry(width=35)
        self.entry_email.grid(column=1, row=2, columnspan=2)
        self.entry_email.insert(0, "sarah-hehn@outlook.de")
        self.entry_password = Entry(width=35)
        self.entry_password.grid(column=1, row=3)
        self.search = Button(text="Search", command=self.search).grid(column=3, row=1)
        self.button_generate = Button(text="Generate Password", command=self.generate).grid(column=3, row=3, padx=0)
        self.button_add = Button(text="Add", width=30, command=self.add).grid(column=1, row=4, columnspan=2)


    def set_controller(self, controller):
        self.controller = controller

    def add(self):
        if self.controller:
            new_data = {
                self.entry_website.get(): {
                    "email": self.entry_email.get(),
                    "password": self.entry_password.get()}
            }
            self.controller.add(new_data)
        self.entry_password.delete(0, 'end')
        self.entry_website.delete(0, 'end')

    def generate(self):
        password = ""
        while len(password) < 15:
            kind = random.choice(CHOOSE_LIST)
            password = password + str(kind[random.randint(0, len(kind) - 1)])
        self.entry_password.insert(0, password)

    def search(self):
        if self.controller:
            data = (self.controller.search(self.entry_website.get()))
            if data is None:
                messagebox.showinfo("Error", "Website not found.")
            else:
                messagebox.showinfo(f"{self.entry_website.get()}", f"Email: {data['email']} \nPassword: {data['password']}")
