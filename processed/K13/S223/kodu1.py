def auto_hind(hind, aastad):
    if aastad == 0: return round(hind,2)
    else: return auto_hind(0.8*hind, aastad-1)
    
#print(auto_hind(6788.46,2)) vastus jääb meelega valeks, sest ma ei oska leida valet vastust, sest see tuleb 4344,6144 ja 4 ei pmardu üles