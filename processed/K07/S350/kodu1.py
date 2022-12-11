def poisse_ja_tüdrukuid(järjend):
    for rida in järjend:
        m=0
        n=0
        if järjend[-1]=="P":
           m=+1
        elif järjend[-1]=="T":
           n=+1
        return(m, n) 
    
