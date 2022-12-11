x = int(input("suured karbid :"))
y = int(input("väiksed karbid : "))
z = int(input("moosi kogus kg-des : "))


def moos(x, y, z):
    i=0
    while True:
        if z >= 5 and x > 0:
            z-= 5
            x-= 1
            i += 1
        elif y > 0 and z > 0:
            y -= 1
            z -=1
            i += 1
        elif z == 0:
            return(i)
        else:
            return(-1)

print(moos(x, y, z))

    
        
    
    