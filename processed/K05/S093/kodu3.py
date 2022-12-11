def moos(x, y, z):
    s = 0
    while True:
        if z >= 5 and x >= 1:       
            z = z - 5
            x = x - 1
            s = s + 1
        else:
            break
    while True:
        if z > 0 and y >= 1:
            z = z - 1
            y = y - 1
            s = s + 1
        else:
            break
        if z == 0:
            return n
        else:
            return -1
        
        


            

    
        
        
    
    