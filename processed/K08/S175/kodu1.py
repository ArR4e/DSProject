import random

from random import sample
sample(range(1, 5), 2)
mitu_arvu = 5
esimesed_kolm_min = 1
esimesed_kolm_max = 10
teised_kaks_min = 11
teised_kaks_max = 20
esimese_kolme_vahe= range(esimesed_kolm_min, esimesed_kolm_max)
teised_kaks_vahe= range(teised_kaks_min, teised_kaks_max)
   
    
def bingo():
    for i in range(mitu_arvu):
        kaart1_3=[]
        kaart1_3 = random.sample(esimese_kolme_vahe, 3)
        while 1 and 2 and 3 in kaart1_3:
            True
            kaart1_3=random.sample(range(1, 10), 3)
            for h in range(mitu_arvu):
                kaart2_5=[]
                kaart2_5 = random.sample(teised_kaks_vahe, 2)
                for j in range(mitu_arvu):
                    bingo_numbrid= ""
                    for k in range(mitu_arvu):
                        bingo_numbrid= kaart1_3 + kaart2_5
                        return bingo_numbrid
                
            
        
    
    