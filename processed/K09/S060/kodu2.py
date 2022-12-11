from random import randint
li=[1,3,3,4,5,5,5,6,6]
def minu_shuffle(järjend):
    a=[]
    h=len(järjend)
    for rida in range(len(järjend)):
        a.append(rida)
    while len(a) >0:
        b=randint(0,len(a)-1)
        l=a.pop(b)
        järjend.append(järjend[l])
    for rida in range(h):
        järjend.pop(0)



        