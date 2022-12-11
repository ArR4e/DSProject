

def rek_abs(a):
    for el in a:
        if isinstance(el,list) == False:
            indeks = a.index(el)
            a[indeks] = abs(el)
        else:
            rek_abs(el)
    return a
            
test = [1,-2,[3,-4],5]

print(rek_abs([]))