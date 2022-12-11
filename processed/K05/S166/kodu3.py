def moos(ska,vka,kmkk):
    ka=0
    while ska>0 and kmkk>0:
        kmkk = kmkk-5
        if kmkk <0:
            kmkk +=5
            break
        ska -=1
        ka +=1
    while vka>0 and kmkk>0:
        kmkk -=1
        vka -=1
        ka +=1
    if kmkk >0:
        return -1
    else:
        return ka