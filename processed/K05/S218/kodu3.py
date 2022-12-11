def moos(suurkarp, väikekarp, kogus):
    
    
    arv = 0
    summa1 = 0
    for i in range(suurkarp):
        kogus = kogus- 5
        summa1= summa1 +1
        if kogus < 5:
            break
    
    
    summa2 = 0


    for i in range(väikekarp):
        kogus = kogus -1
        summa2 = summa2 +1
        if kogus < 1:
            break
        
    if algne == 0:
        arv = 0
    elif algne - (summa1*5 + summa2*1) == 0:
        arv = summa1 + summa2
    elif algne - (summa1*5 + summa2*1) !=0:
        arv = -1
    return arv 
   
suurkarp = int(input("Sisesta suurte karpide arv: "))
väikekarp = int(input("Sisesta väikeste karpide arv: "))
kogus= int(input("Sisesta moosi kogus: "))
algne= kogus


print(moos(suurkarp, väikekarp, kogus))
   
   

    