def moos(s, v, kg):
    
    #Kasutame suured karbid koigepealt
    i = 0
    while s>0 and kg >= 5:
        kg -= 5
        i += 1
        s -= 1
        
    #Kasutame vaikeseid karpe kuniks neid jagub, otsa saamisel ja marjade ule jaamisel kuvame -1
    while kg > 0:
        if v > 0:
            kg -= 1
            i += 1
            v -= 1
        else:
            return(-1)
            
    return(i)
                
print(moos(1, 6, 14))

        
    
    
        
