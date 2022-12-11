def väljasta_liin(e_nimi, j_nimi, sõnastik):
    if j_nimi in sõnastik.keys():
        if e_nimi in sõnastik[j_nimi]:
            print(e_nimi)
            print(j_nimi)
            return True
        else:
            for isik in sõnastik[j_nimi]:
                leidub_liin = väljasta_liin(e_nimi, isik, sõnastik)
                if leidub_liin:
                    print(j_nimi)
                    return True
    return False