def auto_hind(taishind, lainud_aastad):
    if lainud_aastad == 0:
        return taishind
    else:
        lainud_aastad -= 1
        uus_hind = round(taishind * 0.8, 2)
        return auto_hind(uus_hind, lainud_aastad)
print(auto_hind(8000, 5))