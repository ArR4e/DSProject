
def rek_abs(järjend):
    uus = []
    for element in järjend:
        if isinstance(element, int) or isinstance(element, float):
            uus += [abs(element)]   
            
        else:
            uus += [rek_abs(element)]
    return uus


print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))