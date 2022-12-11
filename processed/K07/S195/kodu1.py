def poisse_ja_tüdrukuid(x):
    poistearv = 0
    tydrukutearv = 0
    i = 0
    for i in range(len(x)):
        poistearv += x[i].split().count('P')
        tydrukutearv += x[i].split().count('T')
    v2ljund = [poistearv,tydrukutearv]
    return v2ljund