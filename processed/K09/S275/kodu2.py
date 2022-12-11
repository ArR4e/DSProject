from random import choice
jarjend = []
nrid = []
            
def minu_shuffle(a):
    index = -1
    for i in range(len(a)):
        index += 1
        jarjend.append(index)
        
    while True:
        try:
            random = choice(jarjend)
            nrid.append(a[random])
            jarjend.remove(random)
        except:
            break
    

