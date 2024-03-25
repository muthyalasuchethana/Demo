tup1 = (1, 2, 3.5, "suchi", "pooji", 2)
tup2 = (1, 4, 6, 7, 9.8)
tup3= (3,)
print(tup3)
print(tup2)
print(tup1)

#checking type
print(type(tup1))
print(len(tup1))

#slicing operatinon
print(tup1[1::])

#combiing tuples
tup4 = (tup1, tup2, tup3)
print(tup4)
print(tup4[2])

#length of tuple
print(len(tup4))

tup4 = tup1 + tup2 + tup3
print(tup4)

print(tup1.count(2))
tuple5 = ("suchi",)*5
print(tuple5)
