def rek_abs(a):
    list1 = []
    if isinstance(a, list) == False:
        return abs(a)
    if isinstance(a, list) == True:
        for b in a:
            list1.append(rek_abs(b))
        return list1



#print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))

#print(rek_abs([2, -6]))