def printimine(jär):
    for el in jär:
        print(el)

def väljasta_liin(eel,järg,sug,mag=[]):
    if järg in sug:
        if eel in sug[järg]:
            mag.append(eel)
            mag.append(järg)
            printimine(mag)
            return True
        for inim in sug:
            if eel in sug[inim]:
                mag.append(eel)
                liin = väljasta_liin(inim,järg,sug)
                if liin:
                    return True
                else:
                    break
    return False