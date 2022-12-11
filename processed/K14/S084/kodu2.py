def väljasta_liin(nimi1, nimi2, sugupuu):
    if nimi1 in sugupuu[nimi2]:
        print(nimi1)
        print(nimi2)
        return True
    for i in sugupuu:
        if nimi1 in sugupuu[i]:
            print(nimi1)
            return väljasta_liin(i, nimi2, sugupuu)
    return False

sugupuu = {"Kalle":("Teet", "Maris"),
           "Maris":("Konstantin", "Mari"),
           "Rita":("Teet", "Maris"),
           "Siim":("Teet", "Maris"),
           "Mari":("Karl", "Leeni"),
           "Teet":("Joosep", "Adele"),
           "Adele":("Johannes", "Leida"),
           "Konstantin":("Viktor", "Jelena"),
           "Joosep":("August", "Emma"),
           "Viktor":("Nikolai", "Maria"),}
#print("Kas lii leidub?", väljasta_liin("Mari","Adele",sugupuu))
print("Kas lii leidub?", väljasta_liin("Leida","Kalle",sugupuu))