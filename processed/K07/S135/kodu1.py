def poisse_ja_tüdrukuid(isikud):
    poisidArv = 0
    tydrukudArv = 0
    
    for inimene in isikud:
        inimeneList = inimene.split()
        if inimeneList[-1] == "P":
            poisidArv += 1
        elif inimeneList[-1] == "T":
            tydrukudArv += 1
            
    return (poisidArv, tydrukudArv)