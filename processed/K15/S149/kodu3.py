with open(input("Sisesta failinimi: ")) as f:
    fail = f.readlines()
cancel_sõiduliinid = []
for rida1 in range(len(fail)):
    uus_rida1 = fail[rida1].strip().split()
    uus_rida1 = [int(uus_rida1[0][:2]) + float(uus_rida1[0][3:]) / 60, int(uus_rida1[1][:2]) + float(uus_rida1[1][3:]) / 60, uus_rida1[2]]
    for rida2 in range(len(fail)):
        if rida1 == rida2:
            continue
        uus_rida2 = fail[rida2].strip().split()
        uus_rida2 = [int(uus_rida2[0][:2]) + float(uus_rida2[0][3:]) / 60, int(uus_rida2[1][:2]) + float(uus_rida2[1][3:]) / 60, uus_rida2[2]]
        if uus_rida1[0] > uus_rida2[0] and uus_rida1[1] < uus_rida2[1] and uus_rida1[2] > uus_rida2[2]:
            cancel_sõiduliinid.append(fail[rida2])
        elif uus_rida1[0] < uus_rida2[0] and uus_rida1[1] > uus_rida2[1] and uus_rida1[2] > uus_rida2[2]:
            cancel_sõiduliinid.append(fail[rida1])

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for i in cancel_sõiduliinid:
    if i in fail:
        fail.remove(i)

for rida1 in range(len(fail)):
    punkt1 = fail[rida1].strip().split()
    punkt1 = (int(punkt1[0][:2]) + float(punkt1[0][3:]) / 60, int(punkt1[1][:2]) + float(punkt1[1][3:]) / 60, punkt1[2])
    for rida2 in range(rida1,len(fail)):
        punkt2 = fail[rida2].strip().split()
        punkt2 = (int(punkt2[0][:2]) + float(punkt2[0][3:]) / 60, int(punkt2[1][:2]) + float(punkt2[1][3:]) / 60, punkt2[2])
        if punkt1[1] > punkt2[1]:
            fail[rida1], fail[rida2] = fail[rida2], fail[rida1]
        elif punkt1[1] == punkt2[1] and punkt1[0] > punkt2[0]:
            fail[rida1], fail[rida2] = fail[rida2], fail[rida1]

print("\n".join(fail))