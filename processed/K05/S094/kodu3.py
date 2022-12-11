def moos(big, small, kogus):
    kasutatud_b = 0
    kasutatud_v = 0
    while kogus > 0:
        if big != 0:
            big-=1
            kasutatud_b += 1
            kogus-=5
            if kogus == 0:
                break
            if kogus-5 < 0:
                big = 0                
            continue
        
        if small != 0:
            small-=1
            kasutatud_v +=1
            kogus-=1
            if kogus == 0:
                break
            continue
        
        if big == 0 and small == 0:
            break
    if kogus < 0:
        return -1
    
    if kogus > 0:
        return -1
    else:
        summa = kasutatud_b + kasutatud_v
        return summa

print(moos(5, 0, 3))
