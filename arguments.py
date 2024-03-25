# positioal arguments
def greet(name, dept):
    print(f"hi {name}")
    print(f"are you from {dept} dept")
greet("suchi", "cse")

#keyword arguments
def greet(name, dept):
    print(f"hi {name}")
    print(f"are you from {dept} dept")
greet(dept="cse", name="suchi")



#mixture of positional and keyword
#keyword arguments should follow positional arguments
def greet(name, dept):
    print(f"hi {name}")
    print(f"are you from {dept} dept")
greet("suchi",dept="cse")

#default arguments
def greet(name, subject, dept="cse"):
    print(f"hi {name}")
    print(f"do you  teach {subject}")
    print(f"are you from {dept} dept")
greet("suchi","python")
#this default arguments should be provided before the non_default arguments
def greet(name, subject, dept="cse"):
    print(f"hi {name}")
    print(f"do you  teach {subject}")
    print(f"are you from {dept} dept")
greet("suchi","python","mtech")


#arbytory arguments(*)
def add(*numbers):
    c=0
    for i in numbers:
        c = c+i
    print(f"sum is {c}")
add(1,2,3,4,5,6)

