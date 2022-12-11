s = int(input("Sisesta 5kg karbid: "))
v = int(input("Sisesta 1kg karbid: "))
k = int(input("Sisesta kogus: "))

def moos(a, b, c):
    kar = 0
    while c>=5 and a>0:
        c = c-5
        a = a-1
        kar = kar + 1
    if c == 0:
        return kar
    if b >= c:
        kar = kar + c
        return kar
    else:
        return int(-1)
        
print(moos(s, v, k))