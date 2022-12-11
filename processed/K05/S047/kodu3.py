def moos(suured, väikesed, kogus):
    skarpide_arv=0
    vkarpide_arv=0
    while kogus/5 >= 1:
        if suured > skarpide_arv:
            skarpide_arv=skarpide_arv+1
            kogus=kogus-5
        else:
            break
    while kogus/1 >= 1:
        if väikesed > vkarpide_arv:
            vkarpide_arv=vkarpide_arv+1
            kogus=kogus-1
        else:
            break
    if kogus != 0:
        return (-1)
    else:
        return (vkarpide_arv+skarpide_arv)
    
print(moos(2, 4 ,13))