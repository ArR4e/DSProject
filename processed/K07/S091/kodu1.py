def poisse_ja_tüdrukuid(jarjend):
    poisid = 0
    tydrukud = 0
    for i in range(len(jarjend)):
        element = jarjend[i]
        x = element[::-1]
        if x[0] == 'P':
            poisid += 1
        if x[0] == "T":
            tydrukud += 1
    return(poisid, tydrukud)

x = poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])
print(x)