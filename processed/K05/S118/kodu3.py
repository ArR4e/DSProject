
#funktsioon moos
def moos(suured, väikesed, keedetav_moos):
    #muutuja kasutatud karpide lugemiseks
    kasutatud = 0
    #kui keedetava moosi kaal ei ole täisarv, siis tagastatakse -1
    if keedetav_moos%1 != 0:
        return -1
    #iga while tsükliga lahutatakse keedetavalt moosilt maha suure või väikese karbi mahutatav kogus
    #iga tsükliga lisatakse veel kasutatud karpidele üks juurde
    while keedetav_moos != 0:
        if suured > 0 and keedetav_moos >= 5:
            suured-=1
            kasutatud+=1
            keedetav_moos-=5
            continue
        elif väikesed > 0:
            väikesed-=1
            kasutatud+=1
            keedetav_moos-=1
            continue
        #kui keedetav moos ei mahu täpselt ära või kui seda on liiga palju, tagastatakse -1
        else:
            return -1
    #tagastatakse kasutatud karpide arv
    return kasutatud
            