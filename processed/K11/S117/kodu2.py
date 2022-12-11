#alustasin 11.10.2021 (21:27)
def transponeeriK(maatriks):
    t_maatriks = []
    for i in range(len(maatriks[0])): #vaatame teistpidi, kui oli nt 4 read kus on 2 elementi
        jarjend = []                  #nüüd tahan vaadata, 2 rida kus on 4 elementi
        for j in range(len(maatriks)): 
            jarjend.append(maatriks[j][i]) #vaatame veerud läbi
        t_maatriks.append(jarjend[::-1]) #esimene pöör, sest kõrvaldiagonaal
    return t_maatriks[::-1] #teine pöör, sest kõrvaldiagonaal