def väljasta_liin(e,j,sugupuu):
    if e==j:
        print(e)
        return True
    if j in sugupuu:
        for v in sugupuu[j]:
            if väljasta_liin(e,j,sugupuu):
                print(j)
                return True
    return False
    
