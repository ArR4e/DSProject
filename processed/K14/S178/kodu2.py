

def väljasta_liin1(eellane, järglane, sõnastik):
    if järglane not in sõnastik:
        return(False)
    elif eellane == järglane:
        print(järglane)
        return(järglane)
    else:
        for laps, vanemad in sõnastik.items():
            for element in vanemad:
                if eellane == element:
                    print(eellane)
                    return(väljasta_liin1(laps, järglane, sõnastik))


    

def väljasta_liin(eellane, järglane, sõnastik):
    if väljasta_liin1(eellane, järglane, sõnastik) == False:
        return(False)
    elif väljasta_liin1(eellane, järglane, sõnastik) == None:
        return(False)
    else:
        return(True)
    


print(väljasta_liin('Priit', 'Ene', sõnastik))