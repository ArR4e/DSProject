def poisse_ja_tüdrukuid(list):
    poisse=0
    tudrukuid=0
    for el in list:
        if el[-1]=='P':
            poisse+=1
        elif el[-1]=='T':
            tudrukuid+=1
    return (poisse, tudrukuid)