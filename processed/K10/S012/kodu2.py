#kodutöö 10.2

def võitja(x):
    mängu_seis = {}
    järjestikused_X = ("X", "X", "X")
    järjestikused_O = ("O", "O", "O")
    #Defineerin kõik horisontaalsed read (max 3 el rea kohta, peavad olema järjest)
    rida1a = x[0][:3]
    rida1b = x[0][1:]
    rida2a = x[1][:3]
    rida2b = x[1][1:]
    rida3a = x[2][:3]
    rida3b = x[2][1:]
    rida4a = x[3][:3]
    rida4b = x[3][1:]
    #Defineerin kõik vertikaalsed read
    rida5a = (x[0][0], x[1][0], x[2][0])
    rida5b = (x[1][0], x[2][0], x[3][0])
    rida6a = (x[0][1], x[1][1], x[2][1])
    rida6b = (x[1][1], x[2][1], x[3][1])
    rida7a = (x[0][2], x[1][2], x[2][2])
    rida7b = (x[1][2], x[2][2], x[3][2])
    rida8a = (x[0][3], x[1][3], x[2][3])
    rida8b = (x[1][3], x[2][3], x[3][3])
    #Defineerin kõik diagonaalsed read, milles on vähemalt 3 elementi
    rida9 = (x[1][0], x[2][1], x[3][2])
    rida10a = (x[0][0], x[1][1], x[2][2])
    rida10b = (x[1][1], x[2][2], x[3][3])
    rida11 = (x[0][1], x[1][2], x[2][3])
    rida12 = (x[1][3], x[2][2], x[3][1])
    rida13a = (x[0][3], x[1][2], x[2][1])
    rida13b = (x[1][2], x[2][1], x[3][0])
    rida14 = (x[0][2], x[1][1], x[2][0])
    kõik_read = [rida1a, rida1b, rida2a, rida2b, rida3a, rida3b, rida4a, rida4b,
                 rida5a, rida5b, rida6a, rida6b, rida7a, rida7b, rida8a, rida8b,
                 rida9, rida10a, rida10b, rida11, rida12, rida13a, rida13b, rida14]
    for i in kõik_read:
        if i.count("O") >= 3:
            mängu_seis["O"] = mängu_seis.get("O", 0) + 1
            mängu_seis["X"] = mängu_seis.get("X", 0)
        elif  i.count("X") >= 3:
            mängu_seis["X"] = mängu_seis.get("X", 0) + 1
            mängu_seis["O"] = mängu_seis.get("O", 0)
        else:
            mängu_seis["O"] = mängu_seis.get("O", 0)
            mängu_seis["X"] = mängu_seis.get("X", 0)
    return mängu_seis   
  
