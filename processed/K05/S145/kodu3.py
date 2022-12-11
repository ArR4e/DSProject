def moos(s, v, kg):
    suuredkarbid = 0
    väiksedkarbid = 0
    
    if s * 5 + v < kg:
        return -1
    
    if s > 0:
        while kg > 0:
            kg -= 5
            suuredkarbid += 1
            print(suuredkarbid, kg)
            if suuredkarbid == s:
                break
            elif kg < 5:
                print(kg)
                break
    if v > 0:
        while kg > 0:
            kg -= 1
            väiksedkarbid += 1
            print(väiksedkarbid, kg)
            if väiksedkarbid == v:
                break
        
    if kg == 0:
        return suuredkarbid + väiksedkarbid
    elif kg != 0:
        return -1