def sünnikuupäev(isikukood):
    kuud = ("jaanuar","veebruar","märts","aprill","mai","juuni",
            "juuli","august","september","oktoober","november",
            "detsember")
    
    _isikukood = []
    _isikukood[:0] = isikukood
    
    p = _isikukood[5] + _isikukood[6]
    k = int(_isikukood[3] + _isikukood[4])
    a1 = _isikukood[0]
    a2 = _isikukood[1] + _isikukood[2]
    
    if a1 == "1" or a1 == "2":
        a1 = "18"
    elif a1 == "3" or a1 == "4":
        a1 = "19"
    elif a1 == "5" or a1 == "6":
        a1 = "20"
    elif a1 == "7" or a1 == "8":
        a1 = "21"
        
    a = a1 + a2
    
    return p + ". " + kuud[k-1] + " " + a
