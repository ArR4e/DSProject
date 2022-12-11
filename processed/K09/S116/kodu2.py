from random import randint

a = [1,2,3,3,4,5,6,6,7,7]
def minu_shuffle(a):
    
    for i in range(len(a)):
        x = randint(0, len(a)-1)
        a[i], a[x] = a[x], a[i]
        
    return a

print(minu_shuffle(a))