def rek_abs(järjend,väljund=list(),sügavus=0):
    ajutine = list()
    for el in järjend:
        if isinstance(el, list):
            rek_abs(el,väljund,sügavus+1)
        elif sügavus > 0:
            ajutine.append(abs(el))
        else:
            väljund.append(abs(el))
    if sügavus > 0:
        väljund.append(ajutine)
    return väljund

# def rek_abs(järjend,sügavus=0):
#     global väljund
#     global ajutine
#     if sügavus == 0:
#         väljund = järjend.copy()
#     for indeks,el in enumerate(järjend):
#         if isinstance(el,list):
#             if sügavus > 0:
#                 väljund = ajutine.copy()
#             ajutine = el.copy()
#             uus_el = rek_abs(el,sügavus+1)
#             väljund[indeks] = uus_el
#         elif sügavus > 0:
#             ajutine[indeks] = abs(el)
#         else: väljund[indeks] = abs(el)
#     if sügavus > 0:
#         return ajutine
#     return väljund
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))