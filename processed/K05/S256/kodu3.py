suured = 5 * (int(input("sisesta suurte arv: ")))
väikesed =int(input("sisesta väikeste arv: "))
kogus = int(input("sisesta kogus: "))
def moos (suured, väikesed, kogus):
    if kogus == suured: #suuri on täpselt
        return int(suured / 5)
    if 0 <= kogus - suured <5: #suurtest ei piisa vaja väiksedid
        final = suured / 5 + (kogus - suured)
        return int(final)
    if kogus - suured == kogus:
        if väikesed - kogus >= 0:
            final = kogus
            return int(kogus)
        else:
            return -1 
    if kogus - suured < 0: # suuri jääb üle
        if kogus % 5 <= väikesed: #kas väikeseid on piisavalt
            final = kogus // 5 + kogus % 5
            return int(final)
        else:
            return -1
    else:
        return -1
    
        
    
print(moos(suured, väikesed, kogus))
        