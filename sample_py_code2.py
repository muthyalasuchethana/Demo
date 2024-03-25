# method 1
num1 = 10
num2 = 20
num1, num2 = num2, num1
print(num1, num2)

# method 2
temp1 = num1
num1 = num2
num2 = temp1
print(num1)
print(num2)
