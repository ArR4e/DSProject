

def auto_hind(alghind, aastad):
    if aastad == 0:
        return alghind
    else:
        return auto_hind(round((alghind * 0.8), 2), aastad - 1)
        
#print(auto_hind(10000.0, 5))
#print(auto_hind(8000.0, 5))
#print(auto_hind(10000.0, 1))