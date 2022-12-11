def moos(suuredkarbid, väikesedkarbid, moosikogus):
    kogukarbid = 0
    kogumahtuvus = 5 * suuredkarbid + väikesedkarbid
    
    if moosikogus > kogumahtuvus:
        return -1
    
    while moosikogus >= 5 and suuredkarbid > 0:
        moosikogus -= 5
        kogukarbid += 1
        suuredkarbid -= 1
        
    while 0 < moosikogus and väikesedkarbid > 0:
        moosikogus -= 1
        kogukarbid += 1
        väikesedkarbid -= 1
    
    if moosikogus > 0:
        return -1
    
    else:
        return kogukarbid