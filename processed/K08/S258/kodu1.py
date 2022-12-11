from random import sample
samp1=[]
samp2=[]
for i in range(1,11):
    samp1.append(i)
for i in range(11,21):
    samp2.append(i)
def bingo():
    ret=[]
    ret+= sample(samp1,3)+sample(samp2,2)
    if not (1 in ret and 2 in ret and 3 in ret):
        return ret
    else:
        return bingo()