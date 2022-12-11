suured = int(input("Sisesta suurte karpide arv: "))
väiksed = int(input("Sisesta väikeste karpide arv: "))
kogus = int(input("Sisesta moosi kogus kilogrammides: "))

def moos(suured, väiksed, kogus):

    counter = 0
    while kogus >= 5 and suured != 0:
        kogus -= 5
        suured -= 1
        counter += 1
        
    while kogus >= 1 and väiksed != 0:
        kogus -= 1
        väiksed -= 1
        counter += 1
        
    if kogus == 0:
        return counter
    else:
        return -1
    
print(moos(suured,väiksed,kogus))