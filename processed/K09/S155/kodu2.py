from random import randint
def minu_shuffle(jrj):
    a = len(jrj)-1
    i = 0
    for el in range(len(jrj)):
        suvaline = randint(0,a)
        jrj[i], jrj[suvaline] = jrj[suvaline], jrj[i]
        i += 1
 