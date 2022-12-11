f = open("aadressid.txt",encoding="UTF-8")
tähed = []
kasutajanimed = []
kasutajanimi = False

for rida in f:
    if "ut.ee" in rida:
        for taht in rida:
            if taht == "~":
                kasutajanimi = True
            elif kasutajanimi == True:
                if taht == "/":
                    kasutajanimi = False
                else:
                    tähed.append(taht)
        kasutajanimed.append(''.join(tähed))
        tähed = []

for nimi in kasutajanimed:
    if len(nimi) == 0:
        pass
    else:
        print(nimi)