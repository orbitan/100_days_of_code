import random

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.current_card = ""
        self.current_card_translation = ""
        self.known_words = {}
        self.unknown_words = {}

    def get_next_word(self):
        words = self.model.return_dict()
        self.current_card = random.choice(words)
        self.current_card_translation = self.current_card["English"]
        return self.current_card["Dutch"]

    def get_translation(self):
        return self.current_card_translation

    def add_to_known_words(self):
        print(self.current_card)
        self.model.add_to_next_doc(self.current_card)



