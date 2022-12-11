from random import randint

def minu_shuffle(järj):
    print(järj)
    if len(järj)<2:
        print(järj)
    else:
        kord=randint(10,50)
        while kord>0:
            kord-=1
            pop=järj.pop(randint(0,len(järj)-1))
            järj.insert(randint(0,len(järj)-1),pop)
        print(järj)
#minu_shuffle([1,2,3,4,5,6,7,8,9,10,11])
