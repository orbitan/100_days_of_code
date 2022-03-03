class Animal:
    def __init__(self, name):
        self.eyes = 2
        self.name = name

    def breathe(self):
        print(f"{self.name} is breathing")


class Fish(Animal):
    def __init__(self):
        super().__init__(self.name)

