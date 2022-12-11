#mirjampirn
def väljasta_liin(nimi, jarglane,sonastik):
    if nimi==jarglane:
        print(jarglane)
    else:
        for liin in sonastik:
            print(liin)
            if liin==nimi:
                väljasta_liin(isa,jarglane,sonastik)
                väljasta_liin(ema,jarglane,sonastik)
            else:
                if sonastik[liin][0]==nimi or sonastik[liin][1]==nimi
                laps=liin
                väljasta_liin(laps,jarglane,sonastik)
    return False