import random 

    
#         
    
järjend = [11, 12, 13, 14, 15]
# järjend[1], järjend[2] = järjend[2], järjend[1]
# x = len(järjend)
# juhuslik_arv = random.randint(0, len(järjend))
# y = random.randint(0, 6)
def minu_shuffle(järjend):
    for i in järjend:
        x = järjend.index(i)
        juhuslik_arv = random.randint(0, len(järjend) - 1)
        järjend[x] = järjend[juhuslik_arv]
        uus_list = []
     

print(minu_shuffle(järjend))