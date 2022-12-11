def väljasta_liin(eellane, järglane, sugupuu, printQueue = []):
    for eel, järg in sugupuu.items():
        if eellane in järg:
            printQueue.append(eellane)
            if eel == järglane:
                printQueue.append(eel)
                for i in printQueue:
                    print(i)
                return True
            else:
                return väljasta_liin(eel, järglane, sugupuu, printQueue)
    return False