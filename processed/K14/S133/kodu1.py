def rek_abs(a):
    absoluutväärtus=[]
    for i in range(len(a)):
        if isinstance(a[i], list):
            absoluutväärtus+=[rek_abs(a[i])]
        elif isinstance(a[i], list)==False:
            absoluutväärtus+=[abs(a[i])]
    return absoluutväärtus
#print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))
            