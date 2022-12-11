def transponeeriK(maatriks):
    uus_maatriks = []
    veergude_arv = len(maatriks[0])
    ridade_arv = len(maatriks)
    for i in range(veergude_arv - 1, -1, -1): # Read veeruks
        veerg = [] # Vana rida muutub uueks veeruks
        for j in range(ridade_arv - 1, -1, -1): # Veerud reaks
            veerg.append(maatriks[j][i])
        uus_maatriks.append(veerg) # Lisab uue 'veeru' maatriksi ritta
    return uus_maatriks      