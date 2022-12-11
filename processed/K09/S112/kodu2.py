from random import randint

a = [1,2,3,4,5,6]

def minu_shuffle(a):
    
    for arv in range(len(a) - 1, 0, -1):
        uus = randint(0,arv)
        if uus == arv:
            continue
        a[arv],a[uus] = a[uus],a[arv]
        
minu_shuffle(a)
print(a)
        
#     i = 0
#     for arv in a:
#         i += 1
#         if i <= len(a):
#             a.pop(a.index(arv))
#             a.insert(randint(0,len(a)),arv)
#         else:
#             break
#     return a


