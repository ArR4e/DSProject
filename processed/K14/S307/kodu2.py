def väljasta_liin(eellane, järglane, tree):
    vanemad = list(tree.values())
    vanemad1 = [item for t in vanemad for item in t]
    if eellane == järglane:
        print(eellane)
        return True
    elif eellane not in vanemad1:
        return False   
    else:
        for element in vanemad:
            if element[0] == eellane:
                print (eellane)
                eellane =  (list(tree.keys())[list(tree.values()).index(element)])
                return väljasta_liin(eellane, järglane, tree)
            elif element[1] == eellane:
                print (eellane)
                eellane = (list(tree.keys())[list(tree.values()).index(element)])
                return väljasta_liin(eellane, järglane, tree)
