
def väljasta_liin(eel, järg, puu):
    if järg == eel:
        print(järg)
        return True
    elif järg not in puu:
        return False
    else:
        if väljasta_liin(eel, puu[järg][0], puu) or väljasta_liin(eel, puu[järg][1], puu):
            print(järg)
            return True
        else:
            return False
            
        