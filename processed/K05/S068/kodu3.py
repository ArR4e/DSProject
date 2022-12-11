
def moos(suurkarp,väikekarp,kaal):
    suur=0
    väike=0
    while kaal>= 5 and suurkarp>=1: 
        suurkarp-=1
        suur+=1
        kaal-=5
    while kaal>=1 and väikekarp>=1:
        väikekarp-=1
        väike+=1
        kaal-=1
    if kaal==0:
        return (suur+väike)
    else:
        return(-1)
        
