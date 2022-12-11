def auto_hind(hind, aastad):
    if aastad == 0:
        return hind
    else:
        if aastad > 0:
            #kui auto väärtus langeb 20%, on auto uus hind 100%-20%=80% täishinnast
            uus_hind = round((hind * 80) / 100, 2)
            #kasutades uut hinda arvutab uuesti 80% kuni aastad == 0
            lõpp = round(auto_hind(uus_hind, aastad-1), 2)
        return lõpp

print(auto_hind(8000, 5))