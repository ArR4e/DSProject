from copy import *
def rek_abs(a,x=0):
    if x==0:
        b=deepcopy(a)
    else:
        b=a
    for i in range(len(b)):
        if type(b[i])==list:
            b[i]=rek_abs(b[i],1)
        else:
            b[i]=abs(b[i])
    return b
print(rek_abs([1,3,5,-7,-9,[2,-3,[1,-2]],-8]))