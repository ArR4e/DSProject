def moos (suured,väikesed,kogus):
    suured_vaja = kogus // 5
    suured_kasutada = min(suured_vaja,suured)
    väikesed_vaja = kogus - 5 * suured_kasutada
    if väikesed_vaja <= väikesed:
        return suured_kasutada + väikesed_vaja
    else:
        return -1
    
s = int(input("Palun kirjutage suurte karpide arvu: "))
v = int(input("Palun kirjutage väikeste karpide arvu: "))
k = int(input("Palun kirjutage keedetava moosi koguse kilogrammides: "))

moos (s,v,k)