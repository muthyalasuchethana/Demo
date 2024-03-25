numbers = input("enter list of number:\n")
numbers_list = numbers.split()
count = 0
for number in numbers_list:
    count += 1
print(count)
for i in range(count):
    numbers_list[i]=int(numbers_list[i])
maximum_number = numbers_list[0]
for number in numbers_list:
    if number > maximum_number:
        maximum_number=number
print(f"the maximum number for the given list is {maximum_number}")

