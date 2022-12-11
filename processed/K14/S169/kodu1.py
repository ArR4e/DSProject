def rek_abs(väärtus):
    uus = []
    for a in väärtus:
        if isinstance(a,list) == False:
            uus.append(abs(a))
        else:
            uus.append(rek_abs(a))
    return uus
    
print(rek_abs([]))
    