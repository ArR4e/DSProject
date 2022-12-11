def väljasta_liin(siht, algus, sõnastik):
    if algus in sõnastik and siht in sõnastik[algus]:
            print(siht)
            print(algus)
            return True
    if algus in sõnastik:
        for inimene in sõnastik[algus]:
            if väljasta_liin(siht,inimene,sõnastik):
                print(algus)
                return True
    return False