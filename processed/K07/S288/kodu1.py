def poisse_ja_tüdrukuid(järjend):
    uus_järjend = []
    if len(järjend) == 0:
        return (0, 0)
    for x in järjend:
        tähis = x[-1]
        uus_järjend.append(tähis)
    poisid = uus_järjend.count('P')
    tüdrukud = uus_järjend.count('T')
    return (poisid, tüdrukud)

järjend = input('Sisestage järjend: ')

print(poisse_ja_tüdrukuid(järjend))