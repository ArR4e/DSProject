def rek_abs(j,t=[]):
    for el in j:
        if isinstance(el, list):
            #for i in el:
                #new_i=abs(i)
                #päi = el[0]
                #sab = el[1:]
            t.append(rek_abs(el, []))
            #return rek_abs(saba)
        else:
            new_el=abs(el)
            #päis = j[0]
            #saba = j[1:]
            t.append(new_el)
    return t
#print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))