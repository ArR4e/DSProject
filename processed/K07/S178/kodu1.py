def poisse_ja_tüdrukuid(sisend):
    poisid = 0
    tüdrukud = 0
    for rida in sisend:
        poisid += int(rida.count(' P'))
        tüdrukud += int(rida.count(' T'))
    return(poisid, tüdrukud)

sisend = ()
print(poisse_ja_tüdrukuid(sisend))
