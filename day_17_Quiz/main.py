from data import *
from question_model import *
from QuizBrain import *
from quiz_gui import *

question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank, 0)
gui = QuizGui(quiz)

nq = quiz.next_question()
gui.set_question()



gui.window.mainloop()

