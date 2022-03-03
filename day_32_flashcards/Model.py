import csv
import random

import pandas

DATA = pandas.read_csv("data_files/dutch_english.csv")
TO_LEARN = DATA.to_dict(orient="records")
ONE = pandas.read_csv("data_files/one.csv")


class Model:
    def __init__(self, word):
        self.word = word

    def return_dict(self):
        return TO_LEARN

    def add_to_next_doc(self, unknown):
        with open('data_files/one.csv', 'a') as f_object:
            dictwriter_object = csv.DictWriter(f_object, fieldnames=field_names)

            dictwriter_object.writerow(dict)

            f_object.close()






