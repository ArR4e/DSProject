import random
def minu_shuffle(a):
    for i in range(len(a)-1,0,-1):
       j = random.randint(0,i)
       a[i], a[j] = a[j], a[i]
    #return a


#minu_shuffle([1,2,3,4,5,6])
    