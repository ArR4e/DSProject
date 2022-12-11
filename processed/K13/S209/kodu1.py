def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    else:
        return round(auto_hind(hind * (1 - (20/100)), aastad - 1), 2)
    
v = auto_hind(883123, 2)
print(v)