#programmi päis
def moos(x, y, z):
    purgid = 0 
#programmi keha
    while x > 0 and z >= 5:
        z -= 5
        x -= 1
        purgid += 1
    while y > 0 and z > 0:
        z -= 1
        y -= 1
        purgid += 1
    if z == 0:
        return(purgid)
    else:
        return(-1)

#sisestamised
x = int(input("Sisestage suurte karpide arv: "))
y = int(input("Sisestage väikeste karpide arv: "))
z = int(input("Sisestage keedetava moosi kogus kilogrammides: ")) 

#vastuse saamine
print(moos(x, y, z))