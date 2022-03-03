class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, task):
        self.model.task = task
        self.model.save()






