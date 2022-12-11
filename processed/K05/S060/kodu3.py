def moos(s,v,kogus):
    moosi=0
    kokku=0
    while moosi<kogus:
        if s > 0 and moosi+5 <=kogus:
            moosi=moosi+5
            s=s-1
            kokku=kokku+1
        elif v >0:
            moosi=moosi+1
            v=v-1
            kokku=kokku+1
        else:
            break
    if moosi==kogus:
        return kokku
    else:
        return -1
print(moos(2,6,14))
print(moos(3,3,8))
print(moos(5,1,9))

