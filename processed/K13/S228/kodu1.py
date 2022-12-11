def auto_hind(hind, aastad):
    if aastad == 0: #määran baasi. Kui on möödunud 0 aastat, siis auto hind ei lange.
        hind = round(hind, 2)
        return hind
    else:
        uus_hind = 0.8 * hind #hinna langus 1 aastaga.
        uus_hind = round(uus_hind, 2)
        return auto_hind(uus_hind, aastad - 1)