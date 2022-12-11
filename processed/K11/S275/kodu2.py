def transponeeriK(x):
    a = []
    x.reverse()
    for rida in x:
        rida.reverse()
    print(x)
    for i in range(len(x[0])):
        a.append([])
        
    for j in range(len(x)):
        for k in range(len(x[j])):
            a[k].append(x[j][k])
    return a


