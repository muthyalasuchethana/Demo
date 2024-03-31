class Student:

    def __init__(self, name, roll, age):
        self.name = name        # public instance variable
        self._roll = roll  # protected instance variable
        self.__age = age   # private instance variable

    def __display(self):
        print(f"my self {self.name} {self.__age} years old, My roll_no is {self._roll} ")

    def displayprivatedata(self):
        self.__display()
class Branch(Student):
    pass

def showdata():
    b1 = Branch("suchi", 47,20)
    print(b1.name)
    print(b1._roll)
showdata()
