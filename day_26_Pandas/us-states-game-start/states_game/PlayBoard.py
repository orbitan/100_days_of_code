import turtle
import pandas

class PlayBoard:
    def __init__(self, play_map):
        self.database = pandas.read_csv(f"states_coordinates/{play_map}.csv")
        self.states = self.database["state"]
        self.guessed_states = []
        self.missing_states = []

    def proceed_data(self, answer_state):
        for state in self.states:
            if state.lower() == answer_state.lower():
                xcor, ycor = int(self.database[self.database.state == f"{state}"].x), int(self.database[self.database.state == f"{state}"].y)
                text = f"{state}"
                turtle.goto(xcor, ycor)
                turtle.write(text)
                self.guessed_states.append(answer_state)
        return


    def exit(self):
        self.missing_states = [state for state in self.states if state not in self.guessed_states]
        for state in self.missing_states:
            self.proceed_data(str(state))
