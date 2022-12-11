

def rek_abs(järjend):
    tulemus = []
    for i in järjend:
    #for i in range(len(järjend)):
        if isinstance(i, list):
            tulemus.append(rek_abs(i))
            #return tulemus
        else:
            #print(i)
            tulemus.append(abs(i))
    return tulemus
        
    
print(rek_abs([]))
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))