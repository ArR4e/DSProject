def seosta_lapsed_ja_vanemad(fLapsed,fNimed):
    fLapsed = open(fLapsed)
    fNimed = open(fNimed)
    sõnastik = {}
    vastus = {}
    for rida in fNimed:
        nimi = rida.strip().split(' ', 1)
        sõnastik[nimi[0]] = nimi[1]
    for x in fLapsed:
        iKood = x[12:].strip()
        iKood2 = x[:11].strip()
        nimi = sõnastik[iKood]
        if nimi not in vastus:
            vastus[nimi] = set()
            vastus[nimi].add(sõnastik[iKood2])
        else:
            vastus[nimi].add(sõnastik[iKood2])
    return vastus