import copy
def transponeeriK(a):
    b = copy.deepcopy(a)
    ###pereobraz
    for r in range(len(a)):# dla kazdogo el v a###menaem el na protivopoloznie
        a[r] = b[(len(a)-(r+1))]#     
    d = []
    dd = [] 
    for n in range(len(a[0])):###stolbik teper stroka
        dd = []###ochistka ot proshlogo znachenia
        for i in range(len(a)):###stroka teper stolbik
            dd += [a[i][n]]
        
        d += [dd]
        
    c =copy.deepcopy(d)
    for r in range(len(d)):# dla kazdogo el v d###menaem el na protivopoloznie
        d[r] = c[(len(d)-(r+1))]#
    return d
