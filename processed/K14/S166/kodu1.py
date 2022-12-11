def rek_abs(järjend):
    if type(järjend)!=list:
        return abs(järjend)
    else:
        abs_list=[]
        for el in järjend:
            väärtus=rek_abs(el)
            abs_list.append(väärtus)
        return abs_list