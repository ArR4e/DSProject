def väljasta_liin(vanem, järglane, sugupuu):
    for võti, väärtus in sugupuu.items():
        if võti == järglane:
            if vanem == väärtus[1] or vanem == väärtus[0]:
                print(vanem)
                print(järglane)
                return True
            else:
                if väljasta_liin(vanem, väärtus[1], sugupuu) or väljasta_liin(vanem, väärtus[0], sugupuu):
                    print(järglane)
                    return True
    return False

                
        
    
    
    