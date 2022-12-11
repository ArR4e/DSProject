from copy import deepcopy

def rek_abs(järjend):
    a=deepcopy(järjend)
    for i in range(len(a)):
        if isinstance(a[i], list):
            a[i]=rek_abs(a[i])
        else:
            a[i]=abs(a[i])
    return a