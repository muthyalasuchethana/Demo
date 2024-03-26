class University:

    def __init__(self,uni_name):
        self.uni_name = uni_name

    def show_details(self):
        print(f"uniersity name : {self.uni_name}")

class Course(University):

    def __init__(self,course_name,uni_name):
        University.__init__(self,uni_name)
        self.course_name = course_name

    def show(self):
        print(f"course_name : {self.course_name}, uni_name : {self.uni_name}")

class Branch(University):

    def __init__(self,branch_name,uni_name):
        University.__init__(self,uni_name)
        self.branch_name = branch_name

    def show(self):
        print(f"uni_name : {self.uni_name}, branch_name : {self.branch_name}")

class Student(Course,Branch):

    def __init__(self,uni_name,course_name,branch_name,student_name):
        Course.__init__(self,uni_name,course_name)
        Branch.__init__(self,uni_name,branch_name)
        self.student_name = student_name

    def show(self):
        print(f"uni_name : {self.uni_name}, branch_name : {self.branch_name}, course_name : {self.course_name}, student_name : {self.student_name}")

class Faculty(Branch):

    def __init__(self,uni_name,branch_name,faculty_name):
        Branch.__init__(self,uni_name,branch_name)
        self.faculty_name = faculty_name

    def show(self):
        print(f"uni_name : {self.uni_name}, branch_name : {self.branch_name}, faculty_name : {self.faculty_name}")

uni = University("JNTUA")
uni.show_details()
print(uni.uni_name)
course_1 = Course("Python","JNTUA")
course_1.show()
branch = Branch("JNTUA","CSE")
branch.show()
student = Student("JNTUA","PYTHON","CSE","SUCHI")
student.show()
faculty = Faculty("JNTUA","CSE","pooji")
faculty.show()

