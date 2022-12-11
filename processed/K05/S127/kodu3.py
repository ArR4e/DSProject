def moos(suur, väike, moosi):
    karpe=1
    while moosi>5 and suur>0:
        moosi=moosi-5
        karpe+=1
        suur=suur-1
        return karpe
    if väike>=moosi:
        karpe=karpe+moosi
        return karpe
    else:
        print("-1")
print(moos(5,6,15))