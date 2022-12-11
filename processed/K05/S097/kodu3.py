def moos(suuri_karpe, väikseid_karpe, moosi_kilogrammides):
    
    kasutatud_suuri_karpe = 0
    kasutatud_väikseid_karpe = 0
    allesjäänud_moos = moosi_kilogrammides
    while suuri_karpe >= 1 and allesjäänud_moos >= 5:
        allesjäänud_moos -= 5
        kasutatud_suuri_karpe += 1
        suuri_karpe -= 1
    if allesjäänud_moos <= väikseid_karpe:
        kasutatud_väikseid_karpe = allesjäänud_moos
        return kasutatud_suuri_karpe+kasutatud_väikseid_karpe
    if allesjäänud_moos > väikseid_karpe:
        return -1

