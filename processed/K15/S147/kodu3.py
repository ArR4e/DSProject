def head_bussid(failinimi,head_bussid=list()):
    odavaim = 10000
    vähim_aeg = 10000
    keskmine_aeg = 0
    keskmine_hind = 0
    bussid = dict()
    with open(failinimi,encoding="utf-8") as bussiajad:
        ajad = bussiajad.read().split("\n")
    for rida in ajad:
        minutivahe = int(rida[9:11])-int(rida[3:5])
        täistunnid = int(rida[6:8])-int(rida[:2])
        if minutivahe < 0: #kui minutid lähevad miinustesse, siis tuleb täistunnist lahutada.
            tunnid = täistunnid - round((60-abs(minutivahe))/60,2)
        else: #kui minutivahe on täistunni sees
            tunnid = täistunnid + round(minutivahe/60,2)
        keskmine_aeg += tunnid
        keskmine_hind += int(rida[-1])
        if tunnid < vähim_aeg:
            vähim_aeg = tunnid
        if int(rida[-1]) < odavaim:
            odavaim = int(rida[-1])
        bussid[rida] = (tunnid,int(rida[-1]))
    keskmine_aeg = round(keskmine_aeg/len(bussid),1)
    keskmine_hind = round(keskmine_hind/len(bussid))
    for buss,väärtused in bussid.items():
        if väärtused[0] <= keskmine_aeg and väärtused[1] <= keskmine_hind:
            head_bussid.append(buss)
    for i in range(len(head_bussid)):
        väikseim = i
        for j in range(i+1,len(head_bussid)):
            if head_bussid[väikseim][:2] > head_bussid[j][:2]:
                väikseim = j
            elif head_bussid[väikseim][:2] == head_bussid[j][:2]: #kui sama täistunni sees, siis kummal min varem
                if head_bussid[väikseim][3:5] > head_bussid[j][3:5]:
                    väikseim = j
        head_bussid[i],head_bussid[väikseim] = head_bussid[väikseim],head_bussid[i]
    print("Sobivad bussid on:")
    for aeg in head_bussid:
        print(aeg)

head_bussid(input("Sisesta failinimi: "))