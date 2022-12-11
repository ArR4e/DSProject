def poisse_ja_tüdrukuid(nimed):
    x = (0,0)
    y = list(x)
    for rida in nimed:
        PvT = rida.split(" ")
        if PvT[-1] == "P":
            y[0] = y[0] + 1
        else:
            y[1] = y[1] + 1
    x = tuple(y)
    return (x)
nimed = ['Alo P', 'Andri P', 'Annika T', 'Cristian P', 'Eno P', 'Jaan P', 'Karl Martin P', 'Kert P', 'Kristiina T', 'Magnar P', 'Marion T', 'Meelis P', 'Merilin T', 'Reimo P', 'Silver P', 'Villem P']
print(poisse_ja_tüdrukuid(nimed))