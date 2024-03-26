def lesser_or_greater(a,b):
    if a%2==0 and b%2==0:
        print(min(a,b))
    else:
        print(max(a,b))
lesser_or_greater(2,6)


def same_or_not(str1, str2):
    if str1[0]==str2[0]:
        print(True)
    else:
        print(False)
same_or_not("suchi","akhila")
