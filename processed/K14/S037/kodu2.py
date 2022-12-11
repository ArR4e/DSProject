def väljasta_liin(eellane,järglane,sõnastik):
    
    if järglane not in sõnastik.keys():
        return False
    for võti in sõnastik:
        if sõnastik[järglane][0] == eellane or sõnastik[järglane][1] == eellane:
            print(eellane)
            print(järglane)
            return True
        if eellane == sõnastik[võti][0] or eellane == sõnastik[võti][1]:
            uus_eellane = võti 
            print(eellane)
            return väljasta_liin(uus_eellane,järglane,sõnastik)     
    return False
    
#NB! Ma ei osanud programmi niimoodi kirjutada, et olukorra False 
#puhul programm ei esitaks poolikut liini.