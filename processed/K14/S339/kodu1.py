def rek_abs(järjend):
    if järjend == []:
        return []
    elif not(isinstance(järjend, list)):
        return abs(järjend)
    else:
        abs_järjend = []
        for i in järjend:
            abs_järjend.append(rek_abs(i))
        return abs_järjend
    
    
    
    
    
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))
print(rek_abs([]))
