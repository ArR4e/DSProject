def väljasta_liin(finish, start, sonastik, vastus=[]):
    if vastus == []:
        vastus.append(start)
    if start in sonastik.keys():
        lapsed = sonastik[start] 
        if finish in lapsed:
            vastus.append(finish)
            vastus.reverse()
            for inimene in vastus:
                print(inimene) 
            return True
        else:
            valjund = False
            for laps in lapsed:
                temp = vastus[::]
                temp.append(laps)
                if väljasta_liin(finish, laps, sonastik, temp): 
                    return True
            return False
    else:
        return False