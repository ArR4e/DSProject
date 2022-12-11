def väljasta_liin(eel,jär,sõn):
    if jär==eel:
        print(jär)
        return True
    elif jär in sõn:
        if väljasta_liin(eel,sõn[jär][0],sõn):
            print(jär)
            return True
        elif väljasta_liin(eel,sõn[jär][1],sõn):
            print(jär)
            return True
    return False