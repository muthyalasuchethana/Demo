class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("i can eat")

    def show_details(self):
        print(f"name: {self.name}, age: {self.age} ")

class Male(Human):
    def __init__(self, name, age, location):
        Human.__init__(self, name, age)
        self.location = location

    def sleep(self):
        print("i can sleep")


class Female(Human):
    def __init__(self, name, age, hair):
        Human.__init__(self, name, age)
        self.hair = hair

    def work(self):
        print("i can work")

    def show_details(self):
        Human.show_details(self)
        print(f"hair: {self.hair} ")

female = Female("suchi", 20,"i have long hair")
female.eat()
female.work()
print(female.name)
print(female.age)
print(female.hair)
female.show_details()


male = Male("subhash", 21, "Nellore")
male.sleep()
print(male.location)
print(male.name)
print(male.age)
print(Male.mro())

