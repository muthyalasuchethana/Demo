size = input("what size of pizza do you want (s/m/l)")
bill = 0
if size == "s" :
    bill += 100
    print("small pizza prize is 100$")
elif size == "m":
    bill += 200
    print("medium pizza is 200$")
elif size == "l":
    bill += 400
    print("large pizza is 400$")
add_papperoni = input("do you want to add papperoni(y/n)?\n")
if add_papperoni == "y":
    if size == "s":
        bill += 30
    else:
        bill += 50
add_extracheese = input("do you want to add extra cheese(y/n)?\n")
if add_extracheese == "y":
    if size == "s":
        bill += 30
    else:
        bill += 50
print(f"your final bill is {bill}")
print("enjoy with your food 😊!!")
