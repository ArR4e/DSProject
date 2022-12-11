def transponeeriK(maatriks):
    t_maatriks = []
    for veerg in range(len(maatriks[0])):
        t_maatriks.append([])
        for rida in range(len(maatriks)):
            t_maatriks[veerg].append("")
    for rida in range(len(maatriks)):
        for veerg in range(len(maatriks[rida])):
            t_maatriks[len(maatriks[rida])-veerg-1][len(maatriks)-rida-1] = maatriks[rida][veerg]
    return t_maatriks