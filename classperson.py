class Person:
    def __init__(self, name):
        self.name = name
        print(name)

    def talk(self):
        print(f"hii, I am {self.name} and Yes i talk!")

person = Person("John")
person.name = "Avi"
person.talk()