class Instructor:
    pass


instructor_5 = Instructor()


# print(type(instructor_1))

class Car_Design:
    pass


car_obj1 = Car_Design()
car_obj2 = Car_Design()


# adding two numbers
class Add_Number:
    def __init__(self, number_1, number_2):
        self.number1 = number_1
        self.number2 = number_2


Add_Numbers = Add_Number(20, 30)


# print(Add_Numbers.number1+Add_Numbers.number2)

class Instructor:
    def __init__(self, instructor_name, instructor_address):
        self.name = instructor_name
        self.address = instructor_address
instructor_1 = Instructor("suchi", "Nellore")
print(instructor_1.name)
print(instructor_1.address)
instructor_2 = Instructor("akhila","Delhi")
print(instructor_2.name)
print(instructor_2.address)
