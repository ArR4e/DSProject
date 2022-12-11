a = int(input("Sisestage suurte karpide arv: "))
b = int(input("Sisestage väikeste karpide arv: "))
c = int(input("Sisestage moosi kogus kilogrammides: "))

def moos(a, b, c):
    i = 0
    while True:
        if c >= 5 and a > 0:
            c = c - 5
            a = a - 1
            i = i + 1
        elif c > 0 and b > 0:
            c = c - 1
            b = b - 1
            i = i + 1
        elif c == 0:
            return(i)
        else:
            return(-1)
            
print(moos(a, b, c))