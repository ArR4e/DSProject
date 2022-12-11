skarbid = input("Sisestage suurte karpide arvu: ")
vkarbid = input("Sisestage väikeste karpide arvu: ")
moosikg = input("Sisestage keedetava moosi kogus kilogrammides: ")


while True:
    try:
        skarbid = int(skarbid)
        vkarbid = int(vkarbid)
        moosikg = int(moosikg)
        break
    except:
        skarbid = input("Sisestage suurte karpide arvu: ")
        vkarbid = input("Sisestage väikeste karpide arvu: ")
        moosikg = input("Sisestage keedetava moosi kogus kilogrammides: ")

def moos(skarbid, vkarbid, moosikg):
    
    karbidkokkus  = 0
    karbidkokkuv = 0
    while moosikg > 4:
        moosikg = moosikg - 5
        karbidkokkus  = karbidkokkus + 1
    while moosikg != 0:
        moosikg = moosikg - 1
        karbidkokkuv = karbidkokkuv + 1
    if skarbid - karbidkokkus < 0:
        if vkarbid - karbidkokkuv - ((karbidkokkus - skarbid)*5) >=  0:
            return karbidkokkuv + ((karbidkokkus - skarbid)*5) + skarbid
        else:
            return -1
    elif skarbid - karbidkokkus >= 0 and vkarbid - karbidkokkuv >= 0:
        return karbidkokkuv + karbidkokkus
    else:
        return -1
        

print(moos(skarbid, vkarbid, moosikg))