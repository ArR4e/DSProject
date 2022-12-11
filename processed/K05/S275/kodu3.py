def moos(x, y, z):
    x = 5
    y = 1
    i = 0
    j = 0
    
    if x < z:
        print(-1)
    
    else:
        
        while z >= 5:
            z -= x
            i += 1
        
        while z > 0:
            z -= 1
            j += 1
            
        vastus = i + j
        
        return vastus

