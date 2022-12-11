def auto_hind(hind, aastad):
    if aastad <= 0:
        # tagasta välja arvutatud hind rekursiooni
        # harus (siin ainult 1)
        return hind
    else:
        # 1 - 0.2 = 0.8
        # järgmise_aasta_hind = 0.8 * praeguse_aasta_hind
        return round(auto_hind(0.8*hind, aastad-1), 2)
