def rek_abs(l, tagasi=[]):
    for i in range(len(l)):
        if isinstance(l[i], list)==False:
            tagasi.append(abs(l[i]))
        else:
            tagasi.append(rek_abs(l[i], []))
    return(tagasi)        
