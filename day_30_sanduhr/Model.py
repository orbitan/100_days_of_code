class Model:
    def __init__(self, task):
        self.task = task

    @property
    def task(self):
        return self.__task

    @task.setter
    def task(self, value):
        self.__task = value

    def save(self):
        with open('tasks.txt', 'a') as f:
            f.write(self.task + '\n')
