sk = int(input("Sisestage suurte karpide arv: "))
vk = int(input("Sisestage väikeste karpide arv: "))
mm = int(input("Sisestage keedetavate marjade mass: "))


def moos (sk, vk, mm):
    
    i = 0
    j = 0
    
    if (sk*5 + vk*1) < mm:
        return (-1)

    while sk >0 and mm >0:
        mm -= 5
        sk-=1
        i +=1
        if mm < 5:
            break
            
    while vk > 0 and mm >0:
        mm -=1
        vk-=1
        j+=1
    if mm != 0:
        return -1
        
    return i + j
    
print (moos(sk, vk, mm))

#moos(sk, vk, mm)
#muutuja = moos(sk, vk, mm) et saaksin hiljem i + j gäärtust kasutada!!!
#print (muutuja)