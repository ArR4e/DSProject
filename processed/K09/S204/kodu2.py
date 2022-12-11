
järjend=[]
def minu_shuffle(järjend):
    n=0
    b=järjend[n]
    for b in järjend:
        
        järjend[n], järjend[n+1] = järjend[n+1], järjend[n]
        if n < len(järjend) - 2:
            n+=1
            continue
            
        else:
            break
        
    
        
    
