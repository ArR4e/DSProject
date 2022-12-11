import random
def minu_shuffle(n):
    i=0
    while i < 10000:
        n.append(n.pop(random.randint(0,len(n)-1)))
        i+=1
    
a=[1,2,3,4,5]    
minu_shuffle(a)
print(a)