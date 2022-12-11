

def loetleFilmid(zanr):
    f=open("filmid.txt", encoding="UTF-8")

    filmid_zanrid=[]
   
    for rida in f:
        filmid_zanrid=filmid_zanrid+[rida.strip().split(" - ")]
    if filmid_zanrid==[]:
        filmid=[]
    else:
        
        zanrid=[]
        for el in filmid_zanrid:
             if el[1] not in zanrid:
                zanrid=zanrid+[el[1]]
        
        filmid=[]
        if zanr in zanrid:
            for element in filmid_zanrid:
                if element[1]==zanr:
                    filmid=filmid+[element[0]]
        
        #print(filmi_loetelu)
        elif zanr not in zanrid:
            print("Selle zanriga filme pole.")
    f.close()
    return filmid

# test= loetleFilmid("märul")
# print(test)

def lisaFilm(nimi, zanr):
    f=open("filmid.txt", "a", encoding="UTF-8")
    uus_jarjend1=[nimi]+[zanr]
    uus_tekst=(' - ').join(uus_jarjend1)
#    print(uus_tekst)
    f.write("\n"+uus_tekst)
    
    f.close()
# nimi="Last Vegas"
# zanr= "komöödia"
# test2=lisaFilm(nimi, zanr)
# # 
# # 
# # 
# # 
def kustutaFilm(nimi):
    f=open("filmid.txt", "r", encoding="UTF-8")
    filmid_ja_zanrid=[]
    for rida in f:
        filmid_ja_zanrid=filmid_ja_zanrid+[rida.strip().split(" - ")]
   # print(filmid_zanrid)
    for element in filmid_ja_zanrid:
        #print(element)
        if nimi in element:
            #print(element + ["!"])
            filmid_ja_zanrid.remove(element)
            print("Sinu poolt etteantud film '"+nimi+"' sai kusutatud.")  
        else:
            filmid_ja_zanrid=filmid_ja_zanrid
    #print(filmid_ja_zanrid)
    
    f.close()
    f=open("filmid.txt", "w+", encoding="UTF-8")  
    uuendatud_tekst=""
    for element in filmid_ja_zanrid:
        uuendatud_tekst= uuendatud_tekst + " - ".join(element)+"\n"       
    #print(uuendatud_tekst)
    for line in uuendatud_tekst:
        f.write(line)           
    f.close()
    
# test3= kustutaFilm('Blade Runner')
# print(test3)
#     

# # b = [3, 6, 7, 8, 6]
# # 
# # b.remove(6)
# # print(b)
# 
# 
