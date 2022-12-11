nimiK = input("Sisesta kasutajaimi: ")

def samapass():
    võrdne = False
    w = 1
    while w < 4:
        while võrdne == False:
            ss = input("Sisesta salasõna: ")
            ss2 = input("Sisesta salasõna uuesti: ")
            if (ss == ss2):
                võrdne = eeskiri(ss)
            else:
                print("Salasõnad ei ühti")
                w += 1
    return ss
        
def eeskiri(ss):    
    if len(ss) >= 8:
        for x in ss:
            if any(x.isdigit() for x in ss):
                return True
        else:
            print("Salasõna ei sisalda numbreid")
    
    else:
        print("Salasõna liiga lühike")


ss = samapass()
Tagurpidiss = "".join(reversed(ss))

f = open('users.txt','w+')
f.write(f'nimiK: {nimiK}\nss: {Tagurpidiss}')
f.close()
