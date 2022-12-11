from random import randint
def minu_shuffle(a):
    if a != []:
        segamisi = randint(10,20)
        for i in range(segamisi):
            koht1 = randint(0,len(a)-1)
            koht2 = randint(0,len(a)-1)
        
            väärtus = a[koht2]
        
            a[koht2] = a[koht1]
            a[koht1] = väärtus

print(minu_shuffle([1, 3, 3, 4, 5, 5, 5, 6, 6]))