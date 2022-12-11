# Moosi keetmine

def moos(suured_karbid, väiksed_karbid, moosikilod):
    kasutatud_karbid = 0
    for i in range(suured_karbid):
        if moosikilod < 5:
            break
        moosikilod -= 5
        kasutatud_karbid += 1
    for i in range(väiksed_karbid):
        if moosikilod == 0:
            break
        moosikilod -= 1
        kasutatud_karbid += 1
    if not moosikilod == 0:
        return -1
    return kasutatud_karbid
    
    
    