karp_5kg = int(8)
karp_1kg = int(13)
moosi_kg = int(53)

def moos(suuri_karpe, väikseid_karpe, moosi_kg):
    import math
    suuri_karpe_kulub = 0
    väikseid_karpe_kulub = 0

    #Mitu suurt karpi läheb vaja?
    for karpe in range(suuri_karpe):
        if moosi_kg >= 5:
            moosi_kg -= 5
            suuri_karpe_kulub += 1

    for karpe in range(väikseid_karpe):
        if moosi_kg > 0:
            moosi_kg -= 1
            väikseid_karpe_kulub += 1

    if moosi_kg > 0:
        return -1
    else:
        return suuri_karpe_kulub + väikseid_karpe_kulub

print(moos(karp_5kg,karp_1kg,moosi_kg))