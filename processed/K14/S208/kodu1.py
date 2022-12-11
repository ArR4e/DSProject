import copy
def rek(jrj):
    for i in range(len(jrj)):
        if isinstance(jrj[i], list) == True:
            rek(jrj[i])
        else:
            jrj[i] = abs(jrj[i])
    return jrj
def rek_abs(jrj):
    uusjrj = copy.deepcopy(jrj)
    return rek(uusjrj)