def poisse_ja_tüdrukuid(ennik):
    poisid = 0
    tüdrukud = 0
    for element in ennik:
        if element.endswith(" P"):
            poisid += 1
        if element.endswith(" T"):
            tüdrukud += 1
    
    return (poisid, tüdrukud)