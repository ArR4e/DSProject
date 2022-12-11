import os

def takso(km):
    f = open("taksohinnad.txt", "r")
    if os.stat("taksohinnad.txt").st_size != 0:
        result = []
        for line in f:
            data = line.strip().split(',')
            result.append(data)
        f.close()
    else:
        return None
    
    min_hind = 0
    month = ""
    
    for i in result:
        hind = float(i[1]) + float(i[2]) * km
        if min_hind == 0:
            min_hind = hind
            firma = i[0]
        elif hind < min_hind:
            min_hind = hind
            firma = i[0]
        else:
            continue
    return firma
    

tee = float(input("Sisesta tee pikkus kilomeetrites: "))
print(takso(tee))
