def auto_hind(hind, aastad):
    if aastad == 0: #kui aastad otsa saavad, siis lõpetab fraktaliseerimise
        return round(hind,2)
    else: #kui auto on vana
        return auto_hind(hind*0.8,aastad-1) #hind läheb 20% madalamaks ja aasta edasi
    
print(auto_hind(10000.0,4))
