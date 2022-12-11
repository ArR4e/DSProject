def minu_shuffle(jarjend):
    from random import randint
    jarjend_1=jarjend
    jarjend=[]
    a=1
    for el in jarjend_1:
        jarjend.insert(a,el)
        a=randint(0,len(jarjend_1)-1)