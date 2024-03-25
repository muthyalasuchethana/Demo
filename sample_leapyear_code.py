year = int(input("enter a year : \n"))
if year%4==0:
    if year%100==0:
        if year%400==0:
             print("it is a leap year")
        else:
            print("not a leap year")
    print("it is a leap year")
else:
    print("not a leap year")
