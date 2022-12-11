def moos(x, y, z):
    kasutatud = 0
    while x > 0 and z >= 5:
        z -= 5
        x -= 1
        kasutatud += 1
    while y > 0 and z > 0:
        z -= 1
        y -= 1
        kasutatud += 1
    if z == 0:
        return kasutatud
    else:
        return -1
x = int(input("Sisestage suurte karpide kogus: "))
y = int(input("Sisestage väikeste karpide kogus: "))
z = int(input("Sisestage moosi kogus: "))
print(moos(x, y, z))