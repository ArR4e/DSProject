def transponeeriK(m):
    tm = []
    for i in range(len(m[0])):
        el = []
        for j in range(len(m)):            
            el.append(m[-(j+1)][-(i+1)])
        tm.append(el)
    return tm
            
#print(transponeeriK([[4, 31, 67, 99]]))