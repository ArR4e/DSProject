def moos(skarp, vkarp, kg):
    skarp_uus = int(kg/5)
    
    if skarp >= skarp_uus:
        vkarp_uus = kg-(skarp_uus*5)
    else:
        vkarp_uus = kg
    if skarp >= skarp_uus:
        if vkarp >= vkarp_uus:
            return skarp_uus + vkarp_uus
        else:
            return -1
    else:
        if vkarp >= vkarp_uus:
            return vkarp_uus
        else:
            return -1
        
        



    