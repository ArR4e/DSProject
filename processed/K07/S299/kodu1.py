def poisse_ja_tüdrukuid(järjend):
    poisse=0
    tüdrukuid=0
    for element in järjend:
        if element[-1]=='P':
            poisse += 1
        elif element[-1]=='T':
            tüdrukuid += 1
    return (poisse, tüdrukuid)         