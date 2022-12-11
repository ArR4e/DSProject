def järjesta_punktid(info):
    for i in range(len(info)):
        kes = info[i]
        minnike1 = kes[0]
        minnike2 = kes[1]
        for j in range(i+1, len(info)):
            if info[j][0] < minnike1:
                kes2 = info[j]
                minnike1 = kes2[0]
            elif info[j][0] == minnike1:
                if info[j][1] < minnike2:
                    kes2 = info[j]
                    minnike1 = kes2[0]
                    minnike2 = kes2[1]
        if info[i][0] != minnike1:
            index = index = len(info) - list(reversed(info)).index((kes2)) -  1
            info[i], info[index] = info[index], info[i]
        elif info[i][1] != minnike2:
            index = info.index(kes2) 
            info[i], info[index] = info[index], info[i]
    info = list(dict.fromkeys(info))
    return info

def milline(failinimi):
    info = []
    väärtused = {}
    with open(failinimi) as fail:
        for rida in fail:
            osa = rida.strip() 
            osad = rida.strip(). split(" ")
            väljumine = osad[0].split(":")
            saabumine = osad[1].split(":")
            hind = int(osad[2])
            minutidv = int(väljumine[1])/60
            minutids = int(saabumine[1])/60
            aeg = ((int(saabumine[0])+minutids)-(int(väljumine[0])+minutidv))
            info.append((aeg,hind))
            if (aeg,hind) not in väärtused:
                väärtused[(aeg,hind)] = []
                väärtused[(aeg,hind)].append(osa)
            else:
                väärtused[(aeg,hind)].append(osa)
    x = järjesta_punktid(info)
    for paar in x:
        for ajad in väärtused[paar]:
            print(ajad)
    
failinimi = input("Sisesta busside sõiduplaani fail: ")
print("Bussid on järjestatud nii, et see oleks odav, aga samas kiire, vali endale sobib:")
milline(failinimi)
