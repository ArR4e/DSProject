import random
def minu_shuffle(a):
    jär = a
    jär2 = random.sample(jär, len(jär))
    a.clear()
    for rida in jär2:
        a.append(rida)
a=[1,2,3,4,5,6,7,8,9]
print(minu_shuffle(a))