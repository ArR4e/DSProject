def loetleFilmid(žanr):
    a=[]
    f=open("filmid.txt", encoding="utf-8")
    for rida in f:
        info = rida
        filmi_info=info.split('-')
        filmi_žanr=filmi_info[1]
        filmi_nimi=filmi_info[0]
        if filmi_žanr == žanr:
            a=a+[filmi_nimi]
            print(a)
        else:
            break
            
        print(a)
    f.close()
    
    
def lisaFilm(nimi, žanr):
    f=open("filmid.txt", 'a+', encoding="utf-8")
    f.write(nimi, ' - ', žanr)
    
    f.close()
    
    
def kustutaFilm(nimi):
    f=open("filmid.txt", "r+", encoding="utf-8")
    e=f.readlines()
    f.seek(0)
    for rida in e:
        if nimi not in rida:
            f.write(rida)