def väljasta_liin(eel, j2rg, puu):
    for nimed in puu:
        if eel in puu[nimed]:
            print(eel)
            if (nimed == j2rg):
                print(j2rg)
                return True
            else:
                return väljasta_liin(nimed, j2rg, puu)
    return False