from random import randint

def suurväike(sone):
    #!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
    kirjavahemargid=["!","$","?","|","~","(",")","%",":","<",">","&","+","-",".",";",",","@","^","_","{","}","/","*","`","=","\\","[","]","'",'"','"\"']
    kirja_vahetus_pikkus=int(len(kirjavahemargid))
    asendus_nr=randint(0,kirja_vahetus_pikkus)
    asendus=kirjavahemargid[asendus_nr]                 
    uus_sone=[]
    
    for i in range(len(sone)):
        sone_el=sone[i]
        if sone_el in kirjavahemargid:
            uus_sone.append(asendus)
        elif sone_el==" ":
            uus_sone.append(" ")
        else:    
            sone_up=sone[i].upper()
            sone_low=sone[i].lower()
            
            if sone_el==sone_up:
                uus_sone.append(sone_low)
            elif sone_el==sone_low:
                uus_sone.append(sone_up)
    
    sona=""
    for j in range(len(uus_sone)):
        sona=sona+uus_sone[j]
    
    return(sona)
    
            