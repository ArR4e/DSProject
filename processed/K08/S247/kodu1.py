# argumentideta funktsioon
# järjendina 2 arvu
# 3: 1-10
# 2:- 11-20
# EI tohi lubada olukorda, kus jarj, 1,2,3
# 1-3liiget sum([1,2,3]) == 6
# sellisel juhul genereerin uued arvud
# järjend = []
# 
# def bingo():
#     for el in järjend:
#         sample(range(1,10),3)
# 
# esimene_järjend = sum([1,2,3])
# if sum([1,2,3])! = 6:
#     järjend = järjend + esimene_järjend
#     print(järjend)
# else:
#     sample(range(1,10),3)
#     break
    
# else:
#     järjend = järjend + [1,4]:
#break
# järjend1 = []
# järjend2 = []

#     returnid peavad olema print asemel
from random import sample

def bingo():
    while True:
        järjend2 = []
        n2 = sample(range(11,21),2)
        järjend2 = järjend2 + n2
        järjend1 = []
        n1 = sample(range(1,11),3)
        järjend1 = järjend1 + n1
        if sum(järjend1) !=6:
            järjend = järjend1 + järjend2
            return järjend
print(bingo())






        

    
    
    
    
    