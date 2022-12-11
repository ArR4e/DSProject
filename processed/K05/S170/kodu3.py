suured = 5
väikesed = 1
kogus = 9

def moos(suured, väikesed, kogus):
    karbid = 0
    suurtemaht = suured * 5
    mahub = suurtemaht + väikesed
    if mahub <= kogus:
        return ("-1")
    else:
        while kogus > 0:
            if kogus >= 5:
                if suured > 0:
                    kogus -= 5
                    suured -= 1
                    karbid += 1
            elif väikesed > 0:
                kogus -= 1
                väikesed -= 1
                karbid += 1
            else:
                return("-1")
                
        return karbid     
        
print(moos(suured, väikesed, kogus))
