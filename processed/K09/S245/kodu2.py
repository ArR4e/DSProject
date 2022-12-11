import random

x = []

n = int(input('Sisestage elementide arv listis: '))

for i in range (0,n):
    print('Sisestage element nr:{} '.format(i+1))
    element = int(input())
    x.append(element)
print('Sisestatud list on: \n', x)


def minu_shuffle(x):
    a = [x.append(x.pop(random.randint(0,len(x)-1))) for n in range(len(x))]
    print(a)
    

minu_shuffle(x)
        
#Kuskil peab olema mingi viga, et ta ainult näitab NONE-i

  








        
    
    
    

    
    