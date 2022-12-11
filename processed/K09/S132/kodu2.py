from random import randint

def minu_shuffle(jarjend):
    for i in range(len(jarjend)):
        uus_i = randint(0,len(jarjend)-1)
        jarjend[i], jarjend[uus_i] = jarjend[uus_i], jarjend[i]
        
        
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
minu_shuffle(a)
print(a)