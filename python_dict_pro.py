students_marks = {
    "suchi" : 100,
    "pooji" : 92,
    "akhi" : 82,
    "rohi"  : 72,
    "hruthi" : 60,
    "sruthi" : 50,
    "akhila" : 40,
    "aswini" : 30
}
students_grades = {}
for student in students_marks:
    marks = students_marks[student]
    if marks > 90:
        students_grades[student] = "A+"
    elif marks > 80:
        students_grades[student] = "A"
    elif marks > 70:
        students_grades[student] = "B"
    elif marks > 60:
        students_grades[student] = "C"
    elif marks > 50:
        students_grades[student] = "D"
    elif marks < 50:
        students_grades[student] = "F"
print(students_grades)
