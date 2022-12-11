def rek_abs(jrn):
    uusjrn = []
    if type(jrn) == list:
        for i in jrn:
            uusjrn.append(rek_abs(i))
        return uusjrn
    else:
        return abs(jrn)
            
        
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))
    