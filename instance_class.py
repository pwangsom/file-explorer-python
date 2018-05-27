class InstanceObject:

    name = ""

    def __init__(self, name):
        self.x = 'Hello'
        self.name = name

    def hello(self):
        print(self.x + ' ' + self.name)

