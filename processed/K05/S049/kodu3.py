a = int(input())
b = int(input())
c = int(input())

def moos(karp5, karp1, moos):
    palju5 = moos // 5
    if palju5 > karp5:
        palju5 = karp5 
    palju1 = moos - palju5*5
    if palju1 <= karp1:
        return(palju5+palju1)
    else:
        return(-1)
    
print(moos(a, b, c))
    