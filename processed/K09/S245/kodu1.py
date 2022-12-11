import matplotlib.pyplot as plt
from statistics import harmonic_mean
täisarv = int(input('Sisestage täisarv: '))

numbrid = []
fail = open('aktsiad.txt', encoding = 'utf-8')



for algarvud in fail:
    number = float(algarvud.split(",")[-1].strip())
    numbrid.append(number)
#print(numbrid)


def silu_andmed(numbrid, täisarv):
    for keskmistatud in numbrid:
        if numbrid == '':
            break
        print([keskmistatud])
        print(harmonic_mean(numbrid) * täisarv)
        
        
     
silu_andmed(numbrid, täisarv)


fig = plt.figure()
ax = fig.add_subplot()
ax.plot(numbrid, täisarv)

ax.set:xlabel('Hinnad')

plt.show()

   
        
        
        
    






    
    
    
    
    
    




fail.close()