def rek_abs(m):
    o=[]
    for el in m:
        if isinstance(el, list):
            o+=[rek_abs(el)]
        else:
            o+=[abs(el)]
    return o

m=[2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]
#m=[]
#[2, 6, [8, 12, 12, [4, [6], 3]], 7, [3.55, 3.55]]
print(rek_abs(m))