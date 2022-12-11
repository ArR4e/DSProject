def moos(suured, väiksed, moosi):
    suured = int(suured)
    väiksed = int(väiksed)
    moosi = int(moosi)
    if 5 * suured == moosi:
        karpe = suured
    elif 5 * suured > moosi:
        a = 5 * suured        #see, kui palju moosi võime võtta kõigi olemasolevate suurte karpidega
        while True:
            a -= 5            #järjest teeme ühe karbi võrra vähem
            if a == moosi:
                karpe = moosi // 5
                break
            elif a < moosi:
                vaja_väikseid = moosi - a    
                if vaja_väikseid <= väiksed:   #ehk juhul, kui meil on piisavalt väikseid karpe
                    karpe = a // 5 + vaja_väikseid
                    break
                else:
                    karpe = -1
                    break
    else:
        vaja_väikseid = moosi - 5 * suured
        if vaja_väikseid <= väiksed:
            karpe = suured + vaja_väikseid
        else:
            karpe = -1
    return karpe

suured = input("Sisesta suurte karpide arv: ")
väiksed = input("Sisesta väikeste karpide arv: ")
moosi = input("Sisesta moosi kogus: ")

print(moos(suured, väiksed, moosi))
            
