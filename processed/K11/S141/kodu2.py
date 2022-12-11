def transponeeriK(a):
    b = []
    if len(a) == 1:
        for i in range(len(a[0])-1, -1, -1):
            c = []
            for j in range(len(a)):
                c += [a[0][i]]
            b +=[c]
        return b
    else:
        for i in range(len(a[0])-1, -1, -1):
            c = []
            for j in range(len(a)-1, -1, -1):
                c += [a[j][i]]
            b += [c]         
        return b
