def poisse_ja_tüdrukuid(f):
    sugu = []
    
    for rida in f:
        jupid = rida.split()
        
        if len(jupid) > 2:
            sood = jupid[2]
        else:
            sood = jupid[1]
            
        sugu = sugu + [sood]
        p = sugu.count("P")
        t = sugu.count("T")
    while True:
        try:
            return(p, t)
        except:
            return(0, 0)
        
