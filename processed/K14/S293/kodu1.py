järjend=[2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]

def rek_abs(järjend):
    uus=[]
    for i in järjend:
        if isinstance(i,list):
            uus.append(rek_abs(i))
        else:
            uus.append(abs(i))
    return(uus)

print(rek_abs(järjend))