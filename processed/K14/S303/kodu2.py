def väljasta_liin(e_nimi, j_nimi, sonastik):
    if j_nimi in sonastik:
        if e_nimi in sonastik[j_nimi]:
            print(e_nimi)
            print(j_nimi)
            return True
        else:
            if väljasta_liin(e_nimi, sonastik[j_nimi][1], sonastik) or \
               väljasta_liin(e_nimi, sonastik[j_nimi][0], sonastik):
                print(j_nimi)
                return True
            
    return False
