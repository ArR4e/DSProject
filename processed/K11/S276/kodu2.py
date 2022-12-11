def transponeeriK(maatriks):
    uus_maatriks=[]
    uus_rida=[]
    ridade_arv = len(maatriks)
    rida = maatriks[0]
    veergude_arv = len(maatriks[0])
    for uue_maatriksi_rida in range(veergude_arv):
        for uue_maatriksi_veerg in range(ridade_arv):
            for rida in range(len(maatriks)):
                maatriksi_rida = maatriks[rida]
                uus_veeru_nr = len(maatriks)-rida-1
                for veerg in range(len(maatriksi_rida)):
                    element = maatriksi_rida[veerg]
                    uus_rea_nr = len(maatriksi_rida)-veerg-1
                    #kontrollib, kas element on uues maatriksis sellel positsioonil.
                    if uue_maatriksi_rida == uus_rea_nr and uue_maatriksi_veerg == uus_veeru_nr:
                        uus_rida.append(element)
                    #koostab uue rea ja salvestab muutujasse olemasoleva, kui elementide arv reas on võrdne
                    #elementide arvuga algses veerus.
                    if len(uus_rida)==len(maatriks):
                        uus_maatriks.append(uus_rida)
                        uus_rida = []
    return uus_maatriks