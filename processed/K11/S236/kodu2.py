#Kodutöö: 2. Maatriksi transponeerimine kõrvaldiagonaali järgi

def transponeeriK(maatriks):
    transponeeritud = []
    l = []
    m_rida = 0
    if len(maatriks) == 1:
        for el in maatriks[0]:
            transponeeritud.append(el)
        transponeeritud.reverse()
        return [transponeeritud]
    else:
        while m_rida < len(maatriks[0]):
            for rida in maatriks:
                l.append(rida[len(rida) - (m_rida + 1)])
            l.reverse()
            transponeeritud.append(l)
            l = []
            m_rida += 1
    return transponeeritud

print(transponeeriK([[4, 31, 67, 99]]))

#ül kirjeldus jäi segaseks ja ei saanud aru kuidas on oodatud, et lahenduskäik välja näeks.
#Ehk võiksime praktikumis selle ülesande optimaalseima lahenduskäigu koos läbi vaadata

