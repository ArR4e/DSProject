"""
def moos(suured, vaikesed, kogus):
    vajavaikseid = kogus % 5
    print("vajavaikseid: ", str(vajavaikseid)) 
    vajasuuri = (kogus - vajavaikseid)/5
    
    if vajasuuri > suured or vajavaikseid > vaikesed:
        a = vajasuuri - suured
        b = vaikesed - vajavaikseid
        if a < b and vajavaikseid > vaikesed:
            return -1
        elif a < b:
            e = vaikesed - (b-a*5)
            return int(suured + e) 
        #3return -1
    else:
        return int(vajavaikseid + vajasuuri)
"""

def moos(suur, vaike, kogus):
    suured = 0
    vaikesed = 0
    
    while (suured +1)*5 <= kogus and (suured +1) <= suur:
        suured +=1
    if kogus - (suured*5) <= vaike:
        vaikesed = kogus - (suured*5)
    
    else:
        return -1
    return suured + vaikesed
    


print(moos(1, 1, 11))