arv = int(input('Sisestage naturaalarvude hulk: '))

arv2 = arv

if arv2 < 0:
    print('Sisestage positiivne arv!')
    
else:
    sum = 0
    
    while(arv2 > 0):
        sum += pow(arv2, 2)
        
        arv2 -= 1
        
    print('Summa on: ', sum)
    
if arv < 0:
    print('Sisestage positiivne arv!')
    
else:
    sum2 = 0
    
    while(arv > 0):
        sum2 += arv
        arv -= 1
        
    summa = pow(sum2, 2)
    print('Summa on: ', summa)
    
vahe = summa - sum
print('Vahe on: ', vahe)