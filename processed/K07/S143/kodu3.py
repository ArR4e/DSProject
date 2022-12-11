def sünnikuupäev(ik):
    a = ik[5:7]
    b = {'01':'jaanuar','02':'veebruar','03':'märts','04':'aprill','05':'mai','06':'juuni','07':'juuli','08':'august','09':'september','10':'oktoober','11':'november','12':'detsember'}[ik[3:5]]
    c = ['18','19','20','21'][0 if int(ik[0])<=2 else (1 if int(ik[0])<=4 else (2 if int(ik[0]) <= 6 else 3))] + ik[1:3]
    return f"{a}. {b} {c}"
#print(sünnikuupäev("34501234215"))