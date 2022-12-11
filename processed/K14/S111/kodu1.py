a=[2,-6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]
def rek_abs(a):
    for i, el in enumerate(a):
        if isinstance(el, int) or isinstance(el, float):
            a[i]=abs(el)
        else:
            rek_abs(el)
    return a
print(rek_abs(a))       