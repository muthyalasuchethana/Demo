student_data = {
    "suchi":{"roll_no": 547, "age": 20, "course": "python"},
    "akhii": {"roll_no": 535, "age": 21, "course": "c"},
    "rohi": {"roll_no": 546, "age": 22, "course": "c++"},
}
print(student_data)
print(student_data["suchi"])
print(student_data["akhii"])
print(student_data["suchi"]["course"])
student_data["suchi"]["phn_no"]=8897191620
print(student_data)
print(student_data["suchi"])
del student_data["suchi"]["age"]
print(student_data)

#nesting a list with in a dict

class_room = {
    "A": ["suchi", "akhi", "pooji", "hru", "sruthi"],
    "B": ["rohi", "aswini", "teju", "sundhari"]
}
print(class_room)
print(class_room["A"])
