f1=open("lapsed.txt", encoding="utf=8")
f2=open("nimed.txt", encoding="utf=8")

s={}

def seosta_lapsed_ja_vanemad(f1, f2):
    f1 = open("lapsed.txt", encoding="utf=8")
    for rida in f1:
        osad = rida.strip().split(" ")
        f2 = open("nimed.txt", encoding="utf=8")
        for el in f2:
            info=el.strip().split(" ")
            if osad[1] == info[0] and info[1] not in s: 
                lapse_nimi = " ".join(info[1:])
                
                f2uuesti = open("nimed.txt", encoding="utf=8")
                for i in f2uuesti: 
                    info2 = i.strip().split(" ")
                    if osad[0] == info2[0] and lapse_nimi in s:  
                        s[lapse_nimi].append(" ". join(info2[1:]))  
                    elif osad[0] == info2[0] and lapse_nimi not in s:
                        s[lapse_nimi] = [" ". join(info2[1:])] 
                    
    f1.close()
    f2.close()
    for võti, väärtus in s.items():
        print("{}:{}".format(võti,väärtus)) 
    return s
        

seosta_lapsed_ja_vanemad(f1, f2)


    
   

f1.close()
f2.close()
