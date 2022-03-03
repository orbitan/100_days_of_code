from tkinter import *

LIGHT_BLUE = "#b3d8d5"
RED = "#FF0000"
GREEN = "#00ff00"

class QuizGui():
    def __init__(self, quizbrain):
        global correct_img, false_img, q
        self.quizbrain = quizbrain

        self.window = Tk()
        self.window.config(padx=10, pady=10, bg=LIGHT_BLUE)

        self.score = 0

        self.score_label = Label(text=f"Score {self.score}", bg=LIGHT_BLUE)
        self.score_label.grid(column=1)
        self.q_text = "Reserved for all kind of questions"

        self.canvas = Canvas(self.window, width=300, height=300, bg=LIGHT_BLUE, highlightbackground="white")
        self.canvas.grid_propagate(False)

        self.question_label = Label(self.canvas, text=self.q_text, wraplength=400, justify="left", font=("Courier", 15))
        self.q = self.canvas.create_text(150, 150, text=self.q_text, justify="center", width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=35, padx=10, sticky="nsew")

        # Buttons
        correct_img = PhotoImage(file="Buttons//correct_button_resized.png")
        correct_button = Button(self.window, text="Click me", image=correct_img, height=80, width=80,
                                command=self.button_clicked_true)
        correct_button.grid(row=2, column=0)

        false_img = PhotoImage(file="Buttons//false_button_resized.png")
        false_button = Button(self.window, text="Click me", image=false_img, height=80, width=80, command=self.button_clicked_true)
        false_button.grid(row=2, column=1)

    def set_score(self):
        self.score += 1
        self.score_label.configure(text=f"Score: {self.score}")
        self.window.update()

    def set_question(self):
        q = self.quizbrain.next_question()
        self.canvas.itemconfigure(self.q, text=q)
        if q == False:
            self.final_bg()


    def button_clicked_true(self):
        feedback = self.quizbrain.check_answer("True")
        self.feedback_background(feedback)
        self.set_question()

    def button_clicked_false(self):
        feedback = self.quizbrain.check_answer("False")
        self.feedback_background(feedback)
        self.set_question()

    def feedback_background(self, feedback):
        if feedback == "Incorrect":
            self.canvas.configure(highlightbackground=RED)
            self.canvas.update()
            self.canvas.after(1000, self.canvas.configure(highlightbackground="black"))

        else:
            self.canvas.configure(highlightbackground=GREEN)
            self.set_score()
            self.canvas.update()
            self.canvas.after(1000, self.canvas.configure(highlightbackground="black"))


    def final_bg(self):
        print("Reached")
        self.canvas.itemconfigure(self.q, text=f"You reached the end of the quiz. \nYour score: {self.score}")
        self.window.after(1000, self.window.destroy())





