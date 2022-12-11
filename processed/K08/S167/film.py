#filmidenimekiri

o = open("filmid.txt", "r")
o1 = open("filmid.txt", "r")
#eraldi listid

def genre():
    list = []
    i1 = 0
    while i1<100:
        f = o.readline().strip()
        if f == "":
            break
        d = ""
        for i in f:
            d += i
            if i == " ":
                d = ""
        list.append(d)
    return list

list1 = genre().copy()
#print(list1)
arvlist = list1.copy()

def arv2():
    d = arvlist.pop(0)
    a = len(d)
    return a

def filmid():
    list = []
    i1 = 0
    while i1<100:
        f = o1.readline().strip()
        if f == "":
            break
        
        d = ""
        
        i3 = 0
        arv1 = len(f)
        arv = arv1 - arv2() - 3
        for i in f:
            if i3 == arv:
                break
            i3 += 1
            d += i
        list.append(d)
    return list

list2 = filmid().copy()
#loetlefilmid

def loetleFilmid(x):
    l1 = list1.copy()
    l2 = list2.copy()

    list = []

    countd = l1.count(x)
    i = 0
    while i<countd:
         indeks = l1.index(x)
         nimi = l2[indeks]
         l1.pop(indeks)
         l2.pop(indeks)
         list.append(nimi)
         i += 1
    return list


#print(loetleFilmid("ulme"))

#lisafilm

def lisaFilm(nimi, žanr):
    m = open("filmid.txt", "a")
    string = nimi + " " + "-" + " " + žanr
    m.writelines(["\r", string])
    m.close()    
    return string





#eemalda film

def kustutaFilm(nimi):
#otsing
    o3 = open("filmid.txt", "r")
    i = 0
    while True:
        f = o3.readline().strip()
        arv = len(nimi)
        
        sõna = ""
        
        i1 = 0
        for i2 in f:
            if i1 == arv:
                break
            i1 += 1
            sõna += i2

        if sõna == str(nimi):
            break
        i += 1
    o3.close()

#kustutaja    
    o3 = open("filmid.txt", "r")
    read = o3.readlines()
    arv = i
    
    del read[arv]
    o3.close()
    o4 = open("filmid.txt", "w+")
    
    for rida in read:
        o4.write(rida)
    o4.close()
#-----
#loetleFilmid("krimi"))
#lisaFilm(nimi, žanr)
#kustutaFilm(nimi)