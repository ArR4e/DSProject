def rek_abs(mat):
    uus=[]
    for x in mat:
        if type(x)== type([]):
            uus.append(rek_abs(x))
        else:
            uus.append(abs(x))
    return uus
