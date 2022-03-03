import requests
import html

DATABASE = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean")
QUESTION = DATABASE.json()


class QuizBrain:
    def __init__(self, question_list, score):
        self.question_number = 0
        self.question_list = question_list
        self.score = score
        self.amount_of_questions = 0
        for _ in QUESTION["results"]:
            self.amount_of_questions += 1

    def next_question(self):
        if self.still_has_questions():
            current_question = html.unescape(QUESTION["results"][self.question_number]["question"])
            self.correct_answer = QUESTION["results"][self.question_number]["correct_answer"]
            self.question_number += 1
            return current_question
        else:
            return False

    def still_has_questions(self):
        return self.question_number < self.amount_of_questions

    def check_answer(self, answer):
        if answer.lower() == self.correct_answer.lower():
            return "Correct"
        else:
            return "Incorrect"

        # print("The correct answer is {}".format(correct_answer))
        # print(f"You're current score is {self.score}\n")
