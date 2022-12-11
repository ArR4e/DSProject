from random import randint
def minu_shuffle(jrj):
    for i in range(len(jrj)*randint(2, 6)):
        jrj.insert((randint(0, len(jrj))), jrj.pop(randint(0, (len(jrj)-1))))