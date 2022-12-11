from random import randint

järjend = [1,2,3]

def minu_shuffle(jär):
    for i in range(len(jär)):
        x = randint(0, len(jär)-1)
        nr1 = jär[x]
        nr2 =  jär[i]
        jär[i] = nr1
        jär[x] = nr2
        
minu_shuffle(järjend)
print(järjend)