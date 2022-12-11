from random import randint
def minu_shuffle(järjend):
    try:
        pikkus=len(järjend)
        for i in range(100):
            a=järjend.pop(randint(0, pikkus-1))
            järjend.insert(randint(0, pikkus-1), a)
    except:
        return None
    
