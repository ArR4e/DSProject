def poisse_ja_tüdrukuid(yay):
    P=0
    T=0
    for i in yay:
        if i[-1]=="P":
            P+=1
        else:
            T+=1
    return (P,T)
#saaks ka splitiga teha, aga nii on kergem