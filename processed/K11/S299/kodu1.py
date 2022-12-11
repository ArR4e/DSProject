def seosta_lapsed_ja_vanemad(fail1,fail2):
    nimed={}
    lapsed={}
    with open(fail1, encoding='UTF-8') as f:
        for rida in f:
            (key,value)=rida.split(' ')
            lapsed[key]=value.strip()
    with open(fail2, encoding='UTF-8') as f:
        for rida in f:
            (key,value)=rida.split(' ',1)
            nimed[key]=value.strip()
    uus={}
    for key in lapsed:
        if lapsed[key] in nimed:
# ei oska lahendada
            
        
    
   