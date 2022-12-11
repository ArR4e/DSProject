test=[2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]

def rek_abs(järj):
    out=[]
    for i in järj:
        if isinstance(i, list):
            out+=[rek_abs(i)]
        else:
            if i>0:
                out+=[i]
            else:
                out+=[-1*(i)]
    return out
rek_abs(test)