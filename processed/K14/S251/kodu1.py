def rek_abs(järjend):
    uus = []
    
    for i in järjend:
        
        if isinstance(i,int) or isinstance(i,float):
            uus.append(abs(i))
        elif isinstance(i,list):
            uus.append(rek_abs(i))
    return uus

print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))