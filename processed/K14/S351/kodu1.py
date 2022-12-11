def rek_abs(järjend):
    vastus=[]
    if type(järjend)==list:
        for i in järjend:
            vastus.append(rek_abs(i))
        return vastus
    else:
        return abs(järjend)