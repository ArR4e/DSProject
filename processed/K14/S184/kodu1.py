def rek_abs(järjend):
    uus_järjend=[]
    for i in järjend:
        if isinstance(i, list) is True:
            uus_järjend.append(rek_abs(i))
        else:
            uus_järjend.append(abs(i))
    return uus_järjend
        
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))