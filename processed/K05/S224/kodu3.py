x = int(input("5kg karbid: "))
y = int(input("1kg karbid: "))
z = int(input("Moosi kogus: "))

def moos(x, y, z):
    karpe = 0
    while z >= 5 and x > 0:
        z = z - 5
        x = x - 1
        karpe = karpe + 1
    if z == 0:
        return karpe
    if y >= z:
        karpe = karpe + z
        return karpe
    else:
        return int(-1)
    
print(moos(x, y , z))
        
        
        