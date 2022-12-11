def väljasta_liin(eel, järg, dic):
    try:
        laps = järg
        isa = dic[järg][0]
        ema = dic[järg][1]
        if isa == eel or ema == eel:
            print(eel)
            print(laps)
            return True
        else:
            if väljasta_liin(eel, ema, dic) == True:
                print(laps)
                return True
            if väljasta_liin(eel, isa, dic) == True:
                print(laps)
                return True
        return False
    except:
        return False 
            
       
        
        
        
