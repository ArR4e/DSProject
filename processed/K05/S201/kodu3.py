a = int(input("Sisesta suurte karpide arv: "))
b = int(input("Sisesta väikeste karpide arv: "))
c = int(input("Siseta keedetava moosi kogus kilogrammides: "))
def moos(a,b,c):
    karbid = 0
    jaak = 0
    if c<5 and c<=b :
        karbid =+ c
    if c >= 5 and c // 5 <= a:
        karbid =+ c // 5
        jaak =+ c % 5
    elif c // 5 > a :
        karbid =+ a
        jaak =+ c- a*5 
    if jaak > 0 and jaak <= b:
        karbid = karbid + jaak
    if jaak > b :
        return int(-1)
    elif c == 0:
        return int(0)
    elif karbid >0 and jaak <= b:
        return(karbid)
    elif jaak>0:
        return int(-1)
    else:
        return int(-1)    
print(moos(a,b,c))