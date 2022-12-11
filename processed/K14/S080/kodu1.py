def rek_abs(järjend):
    listike = []
    
    for element in järjend:
        if isinstance(element,list):
            listike.append(rek_abs(element))
        else:
            listike.append(abs(element))
    
    return listike
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))
