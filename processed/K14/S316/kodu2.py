def väljasta_liin(eellane,järglane,sugupuu):
    try:
        print(eellane)
        for võti,vanemad in sugupuu.items():
            if eellane == järglane:
                break
            elif eellane in vanemad[0]:
                eellane = võti
                väljasta_liin(eellane,järglane,sugupuu)
            elif eellane in vanemad[1]:
                eellane = võti
                väljasta_liin(eellane,järglane,sugupuu)
        return True
    except:
        return False