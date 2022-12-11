def väljasta_liin(eel, jarg, sonastik):
    try:
        vanemad =  sonastik[jarg]
        if eel in vanemad:
            print(eel)
            return True
        else:
           for i in vanemad:
               if väljasta_liin(eel, i, sonastik):
                   print(i)
                   return True
               else:
                    continue
    except:
        return False