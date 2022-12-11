def transponeeriK(lst):
    uus = []
    for i in lst:
        i.reverse()
    lst.reverse()
    for i in range(len(lst[0])):
        uus.append([])
        for j in lst:
            uus[i].append(j[i])
    return uus