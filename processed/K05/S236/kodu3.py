#Moosi keetmine

karbid = 0

def moos(a, b, c):
    while c > 0:
        
        if a < 0 and (c - a) > 0:
            a = c - 5
            karbid += 1
            
        if b >= c:
            b = c - 1
            karbid += 1
        else:
            print("-1")
            break
    print(karbid)