
            
def seosta_lapsed_ja_vanemad(lastefail,nimedefail):
    vanem_laps={}
    nimeddic={}
    with open(nimedefail, "r") as f:
         for rida in f:
             nimed=rida.strip().split(' ',1)
             nimeddic[nimed[0]]=nimed[1]
             
    with open(lastefail, "r") as f:
        for rida in f:
            lapsed= rida.strip().split()
            if nimeddic.get(lapsed[1]) in vanem_laps:
                vanem_laps[nimeddic.get(lapsed[1])].add(nimeddic.get(lapsed[0]))  
            else:
                vanem_laps[nimeddic.get(lapsed[1])] = set([nimeddic.get(lapsed[0])])

    return vanem_laps

sõnastik = seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')

    

for võti,väärtus in sõnastik.items():
    järjend=list(sõnastik.get(võti))
    if len(sõnastik[võti]) == 2:
        print(võti,':',järjend[0],',',järjend[1])
    else:
        print(võti,':',järjend[0])

    
        
    
    