
def suurväike(sõne):
    import string
    import random
    pöördsõne1 = sõne.swapcase()
    muudatus = random.choice(string.punctuation)
    for elem in pöördsõne1:
        if elem in string.punctuation:
            print(elem)
            pöördsõne1 = pöördsõne1.replace(elem, muudatus)
        else:
            pöördsõne1 = pöördsõne1
    return pöördsõne1


print(suurväike(".,:;!?"))
