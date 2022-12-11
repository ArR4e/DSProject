from random import randint
a=[1,2,4,5,3]
def minu_shuffle(a):
    for i in range(len(a)):
        vahetus=randint(0, len(a)-1)
        vv=a[vahetus]
        a[vahetus]=a[i]
        a[i]=vv
minu_shuffle(a)
print(a)