def moos(suuri,väikseid,moosi):
    count=0
    while moosi >= 5 and suuri>0:
        moosi -= 5
        suuri -=1
        count += 1
    if moosi > väikseid:
        return -1
    elif moosi == 0:
        return count
    else:
        return count + moosi
               
            

            
    