def seosta_lapsed_ja_vanemad(lapsed_fail, nimed_fail):
    f_lapsed = open(lapsed_fail, encoding = "utf-8-sig")
    f_nimed = open(nimed_fail, encoding = "utf-8-sig")
    isikukoodid_list = {}
    nimedisikoodidega = {}
    lasteisikukoodid1 = []
    while True:
        rida_nimed = f_nimed.readline().strip()
        if rida_nimed =="":
            break
        rida_nimed1 = rida_nimed.split(" ", 1)
        isikukood = rida_nimed1[0]
        nimi = rida_nimed1[1]
        nimedisikoodidega[isikukood] = nimi
    while True:
        rida_lapsed = f_lapsed.readline().strip()
        if rida_lapsed == "":
            break
        rida_lapsed1 = rida_lapsed.split(" ")
        vanema_isikukood = rida_lapsed1[0]
        lapse_isikukood = rida_lapsed1[-1]
        if lapse_isikukood not in lasteisikukoodid1:
            lasteisikukoodid1.append(lapse_isikukood)
            isikukoodid_list[nimedisikoodidega[lapse_isikukood]] = set()
            isikukoodid_list[nimedisikoodidega[lapse_isikukood]].add(nimedisikoodidega[vanema_isikukood])
        elif lapse_isikukood in lasteisikukoodid1:
            isikukoodid_list[nimedisikoodidega[lapse_isikukood]].add(nimedisikoodidega[vanema_isikukood])
    return isikukoodid_list
    f_lapsed.close()
    f_nimed.close()
  
sõnastik = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for võti in sõnastik:
    vanemad_printimiseks = ", ".join(sõnastik[võti])
    print(võti + ":",vanemad_printimiseks)

    

    