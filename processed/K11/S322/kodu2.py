
def transponeeriK(maatriks):
    transpmaatriks = []
    # alusta paremast veerust, liigu vasakule
    
    # esimene arv on maatriksi rea pikkus, millest saab
    # transponeeritud maatriksis veeru pikkus (ja
    # vastupidi alamtsüklis)
    for veerg in range(len(maatriks[0])-1, -1, -1):
        # transponeeritud maatriksi rida
        uus_rida = []
        # alusta alumiselt realt, liigu üles
        for rida in range(len(maatriks)-1, -1, -1):
            uus_rida.append(maatriks[rida][veerg])
        transpmaatriks.append(uus_rida)
    return transpmaatriks
