def väljasta_liin(eellane,järglane,sugupuu):
    if järglane in sugupuu:
            if sugupuu[järglane][0] == eellane:
                print(eellane)
                print(järglane)
                return True
            elif sugupuu[järglane][1] == eellane:
                print(eellane)
                print(järglane)
                return True
            else:
                if väljasta_liin(eellane,sugupuu[järglane][0],sugupuu) == True:
                    print(järglane)
                    return True

                elif väljasta_liin(eellane,sugupuu[järglane][1],sugupuu) == True:
                    print(järglane)
                    return True
                else:
                    return False
    else:
       return False
