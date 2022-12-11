#moosi keetmine

def moos(suured, väikesed, kogus):
    if suured==0:
        if väikesed<kogus:
            return -1
        return kogus
    üle=0
    suuri_kasutada=kogus//5
    if suuri_kasutada>suured:
        üle=(suuri_kasutada-suured)*5
        suuri_kasutada=suured
    üle+=kogus%5
    väikeseid_kasutada=üle
    if väikeseid_kasutada>väikesed:
        return -1
    else:
        return suuri_kasutada+väikeseid_kasutada