def moos(x, y, m):
    a = 0
    b = 0 
    if x > 0:
        if x*5 <= m:
            a = x
        else :
            a = m // 5
    b = m -(a*5)
    if y >= b:
        return a + b
    else:
        return -1
    
    
a = int(input())
b = int(input())
c = int(input())

print(moos(a, b, c))
