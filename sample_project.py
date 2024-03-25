class circle:
    pi = 3.14 # class object attribute
    def __init__(self,radius_1):
        self.radius = radius_1
        self.area = circle.pi * (self.radius**2)
    def circum(self):
        return 2 * self.pi * self.radius # self.pi = circle.pi

circum_circle_1 = circle(4)
print(circum_circle_1.circum())
circum_circle_2 = circle(14)
print(circum_circle_2.circum())
print(circum_circle_1.area)

