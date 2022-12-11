def moos(suur,väike,kg):
    suurn = 0
    väiken = 0
    if suur*5+väike < kg:
        return -1
    while kg > 0 and suur != 0 and kg-5 >= 0:
        kg -= 5
        suur -= 1
        suurn +=1
    if kg > 0:
        while kg > 0 and väike != 0 and kg-1 >= 0:
            kg -= 1
            väike -= 1
            väiken += 1
        if kg > 0 and väike == 0:
            return -1
    return suurn+väiken

print(moos(2,6,14))
print(moos(3,3,8))
print(moos(1,2,10))
print(moos(5,1,9))
    
            