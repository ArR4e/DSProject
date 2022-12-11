import random



def minu_shuffle(jarjend):
    for i in range(len(jarjend)-1, 0, -1):
        juhuslik = random.randint(0,i)
        jarjend[i], jarjend[juhuslik] = jarjend[juhuslik], jarjend[i]

    
    
    
jarjend = [22,22,22,22,22]

minu_shuffle(jarjend)
print(jarjend)