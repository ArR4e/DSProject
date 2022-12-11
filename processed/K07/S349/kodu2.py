teekond = float(input("Siseta kilomeetrites enda teekond: "))

def loe_andmed(failinimi):
    nimi = []
    hind = []

    f = open(failinimi, encoding="UTF-8")
    for rida in f:
        rida = rida.strip()
        osad = rida.split(",")
        sõiduvahend = osad[0:-2]
        sisseistumise_hind = osad[-2:-1]
        kilomeetri_hind = osad[-1:]
        nimi = nimi + sõiduvahend
        hind = hind + (sisseistumise_hind + kilomeetri_hind)
    
    f.close()
    
    maksumus_a = float(hind[0]) + float(hind[1]) * teekond
    maksumus_b = float(hind[2]) + float(hind[3]) * teekond
    maksumus_c = float(hind[4]) + float(hind[5]) * teekond
    
    maksumus = [maksumus_a, maksumus_b, maksumus_c]
    väikseim = min(maksumus)
    if väikseim == maksumus [0]:
        return nimi[0]
    elif väikseim == maksumus [1]:
        return nimi[1]
    else:
        return nimi[2]
 
    

print("Kõige odavam takso peaolt koju saamiseks on täna " + loe_andmed("taksohinnad.txt"))




