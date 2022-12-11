def moos(suur,väike,moosi):
    väikseid=0
    if moosi%5!=0:
        suuri=(moosi-(moosi%5))/5
    else:
        suuri=moosi/5 
    if suuri>suur:
        suuri=suur
        väikseid=moosi-5*suuri
    else:
        väikseid=moosi%5
    if (suuri+väikseid)>(suur+väike) or väikseid>väike:
        return -1
    return int(suuri+väikseid)