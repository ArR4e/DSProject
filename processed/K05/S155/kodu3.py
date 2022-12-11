#suurkarp = x
#väikekarp = y
#moos kilogrammides = z

def moos(x, y, z):
    if z // 5 <= x:
        mitu_suurt = z // 5
        jääk = z % 5
        if jääk <= y:
            return mitu_suurt + jääk
        else:
            return -1
    if z // 5 >= x and z - x * 5 // 1 < y:
        return x + z - x * 5
    else:
        return -1

print(moos(2, 3, 13))