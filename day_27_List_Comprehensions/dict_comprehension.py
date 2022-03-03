import random
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
scores = {student:random.randint(1, 101) for student in names}
passed_student = {name:scores[name] for name in scores if scores[name] > 59}
print(passed_student)