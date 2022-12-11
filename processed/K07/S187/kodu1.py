def poisse_ja_tüdrukuid(hulk):
    poisse = 0
    tydrukuid = 0
    for inimene in hulk:
        if inimene[len(inimene) - 1] == "T":
            tydrukuid += 1
        elif inimene[len(inimene) - 1] == "P":
            poisse += 1
    return (poisse, tydrukuid)

