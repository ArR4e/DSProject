from math import sqrt

def transponeeriK(m):
    kõik_el=[]
    rida=0
    elemendid=0
    for i in m:
        rida+=1
        veerud=len(i)
    
    for i in range(veerud):
        for j in range(rida):
            kõik_el.append(m[j][i])
    kõik_el.reverse()
    uus_maatriks=[]
    for x in range(veerud):
        uus_maatriks.append(kõik_el[x*rida:(x+1)*rida])
    return uus_maatriks

print(transponeeriK([[4, 31, 67, 99]]))