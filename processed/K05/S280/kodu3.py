# 3. Moosi keetmine / RP
from math import *

def moos(suur,väike,moos):
    #Vaatame kas on üldse moosi olemas
    if moos == 0:
        return 0
    
    #Arvutame vajatud suurte karpide väärtuse, kui moosi on liiga vähe mitme karbi jaoks, siis mahutame kõik ühte suurde
    suured = floor(moos/5)
    if suured >= 1 and suur >= 1 and suured == suur:
        suured = suured
    elif suured != suur:
        if suured > suur:
            suured = suur
        elif suur > suured:
            suured = suured
    else:
        suured = 0
    
    #Kontrollime, et suuri karpe on piisavalt ja ka lahutame vajaliku moosi
    if suured < 0:
        return -1
    if suur != 0:
        moos -= suured * 5
    
    #Kontrollime palju väikseid karpe on vaja ning kontrollime, et ka nii palju neid on
    väiksed = moos / 1
    if väiksed > väike:
        return -1
    
    #Kontrollime, et oleks vähemalt 1 väikest karpi vaja
    if väiksed / 1 < 1 and moos != 0:
        return -1
    if väike != 0:
        moos -= väiksed
    
    #Arvutame karpide vajaduse kokku
    return int(suured + väiksed)

print(moos(2,6,14))