def moos(suurkarp, väikekarp, moosikogus):
    suurekarbimuutuja=0
    väiksekarbimuutuja=0
    moosikogusemuutuja=0
    #vaatan palju saab suuri karpe kasutada ja palju moosi sellega valmis saab
    while suurekarbimuutuja<suurkarp and moosikogusemuutuja<moosikogus-4:
        suurekarbimuutuja+=1
        moosikogusemuutuja+=5
    #vaatan palju saab väikseid karpe kasutada ja palju moosi sellega valmis saab
    while väiksekarbimuutuja<väikekarp and moosikogusemuutuja<moosikogus:
        väiksekarbimuutuja+=1
        moosikogusemuutuja+=1
    if moosikogusemuutuja!=moosikogus:
        return -1
    else:
        return suurekarbimuutuja+väiksekarbimuutuja
print(moos(5, 1, 9))
