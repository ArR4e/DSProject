def moos(a,b,c):
    if c == a * 5 + b:
        lahend = int(a + b)
        return(lahend)
    elif c == 0:
        lahend = 0
        return(lahend)
    elif c == a * 5 + (b - 1) and b >= 1:
        lahend = int(a + b - 1)
        return lahend
    elif c == a * 5 + (b - 2) and b >= 2:
        lahend = int(a + b - 2)
        return lahend
    elif c == a * 5 + (b - 3) and b >= 3:
        lahend = int(a + b - 3)
        return lahend
    elif c == a * 5 + (b - 4) and b >= 4:
        lahend = int(a + b - 4)
        return lahend
    elif c == a * 5 + (b - 5) and b >= 5:
        lahend = int(a + b - 5)
        return lahend
    elif c == a * 5 + (b - 6) and b >= 6:
        lahend = int(a + b - 6)
        return lahend
    elif c == a * 5 + (b - 7) and b >= 7:
        lahend = int(a + b - 7)
        return lahend
    elif c == a * 5 + (b - 8) and b >= 8:
        lahend = int(a + b - 8)
        return lahend
    elif c == a * 5 + (b - 9) and b >= 9:
        lahend = int(a + b - 9)
        return lahend
    elif c == a * 5 + (b - 10) and b >= 10:
        lahend = int(a + b - 10)
        return lahend
    elif c == (a - 1) * 5 + b and a >= 1:
        lahend = int(a + b - 1)
        return lahend
    elif c == (a - 2) * 5 + b and a >= 2:
        lahend = int(a + b - 2)
        return lahend
    elif c == (a - 3) * 5 + b and a >= 3:
        lahend = int(a + b - 3)
        return lahend
    elif c == (a - 4)* 5 + b and a >= 4:
        lahend = int(a + b - 4)
        return lahend
    elif c == (a - 5) * 5 + b and a >= 5:
        lahend = int(a + b - 5)
        return lahend
    elif c == (a - 1) * 5 + (b - 1) and a >= 1 and b >= 1:
        lahend = int(a + b - 2)
        return lahend
    elif c == (a - 2) * 5 + (b - 2) and a >= 2 and b >= 2:
        lahend = int(a + b - 4)
        return lahend
    elif c == (a - 3) * 5 + (b - 3) and a >= 3 and b >= 3:
        lahend = int(a + b - 6)
        return lahend
    elif c == (a - 4)* 5 + (b - 4) and a >= 4 and b >= 4:
        lahend = int(a + b - 8)
        return lahend
    elif c == (a - 5) * 5 + (b - 5) and a >= 5 and b >= 5:
        lahend = int(a + b - 10)
        return lahend
    elif c == (a - 1) * 5 + (b - 2) and a >= 1 and b >= 2:
        lahend = int(a + b - 3)
        return lahend
    elif c == (a - 2) * 5 + (b - 1) and a >= 2 and b >= 1:
        lahend = int(a + b - 3)
        return lahend
    elif c == (a - 3) * 5 + (b - 1) and a >= 3 and b >= 1:
        lahend = int(a + b - 4)
        return lahend
    elif c == (a - 1)* 5 + (b - 3) and a >= 1 and b >= 3:
        lahend = int(a + b - 4)
        return lahend
    elif c == (a - 2) * 5 + (b - 3) and a >= 2 and b >= 3:
        lahend = int(a + b - 5)
        return lahend
    elif c == (a - 3) * 5 + (b - 2) and a >= 3 and b >= 2:
        lahend = int(a + b - 5)
        return lahend
    elif c == (a - 2) * 5 + (b - 4) and a >= 2 and b >= 4:
        lahend = int(a + b - 6)
        return lahend
    elif c == (a - 4) * 5 + (b - 2) and a >= 4 and b >= 2:
        lahend = int(a + b - 6)
        return lahend
    elif c == (a - 3)* 5 + (b - 4) and a >= 3 and b >= 4:
        lahend = int(a + b - 7)
        return lahend
    elif c == (a - 4) * 5 + (b - 3) and a >= 4 and b >= 3:
        lahend = int(a + b - 7)
        return lahend
    elif c == (a - 1) * 5 + (b - 4) and a >= 1 and b >= 4:
        lahend = int(a + b - 5)
        return lahend
    elif c == (a - 4) * 5 + (b - 1) and a >= 4 and b >= 1:
        lahend = int(a + b - 4)
        return lahend
    elif c == (a - 1) * 5 + (b - 5) and a >= 1 and b >= 5:
        lahend = int(a + b - 6)
        return lahend
    elif c == (a - 5)* 5 + (b - 1) and a >= 5 and b >= 1:
        lahend = int(a + b - 6)
        return lahend
    elif c == (a - 5) * 5 + (b - 2) and a >= 5 and b >= 2:
        lahend = int(a + b - 7)
        return lahend
    elif c == (a - 2) * 5 + (b - 5) and a >= 2 and b >= 5:
        lahend = int(a + b - 7)
        return lahend
    else:
        lahend = -1
        return(lahend)

        


a = int(input("Sisesta suurte karpide arv: "))
b = int(input("Sisesta väikeste karpide arv: "))
c = int(input("Sisesta moosi kogus kilogrammides: "))

print(moos(a,b,c))