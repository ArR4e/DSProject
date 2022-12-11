

def rek_abs(sisend):
    uuslist = []
    for siisend in sisend:
        checker = isinstance(siisend, list)
        if checker == True:
            uuslist.append(rek_abs(siisend))
        
        elif checker == False:
            sisestatav = abs(siisend)
            uuslist.append(sisestatav)
    return uuslist
        
llist =  [2, -1, 4, [-1, -1, -2], [-2, [-2, -1]]]       
print(rek_abs(llist))