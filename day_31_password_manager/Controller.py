class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, password):
        self.model.account = password
        self.model.save(password)

    def search(self, website):
        return self.model.search(website)

    def add(self, data):
        self.save(data)