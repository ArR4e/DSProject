def transponeeriK(m):
    veerud = []
    for i in range(len(m[0])):
        veerg = []
        for rida in m:
            veerg.append(rida[i])
        veerud.append(veerg)

    for i in range(len(veerud)):
        veerud[i].reverse()

    veerud.reverse()

    return(veerud)
        