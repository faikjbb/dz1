class Civilian:
    def __init__(self):
        self.name = "Alex"
        self.age = 18
        self.height = 197
        self.university = "Drawing Uni"

    def AboutMe(self):
        print("My name is " + self.name.__str__())
        print("My age is " + self.age.__str__())
        print("My height is " + self.height.__str__())
        print("My university is " + self.university.__str__())


class Policeman:
    def __init__(self):
        self.name = "Bob"
        self.age = 48
        self.height = 156
        self.university = "Unknown"

    def AboutnotMe(self):
        print("My name is " + self.name.__str__())
        print("My age is " + self.age.__str__())
        print("My height is " + self.height.__str__())
        print("My university is " + self.university.__str__())

Alex = Civilian()
Alex.AboutMe()

Bob = Policeman()
Bob.AboutnotMe()