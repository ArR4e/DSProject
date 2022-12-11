def rek_abs(järjend):
    uusjärjend = []
    for el in järjend:
        if isinstance(el, list):
            uusjärjend.append(rek_abs(el)) 
        else:
            uusjärjend.append(abs(el))
    
    return uusjärjend

järjend = [-1,-2,3,[1,-2,-3,[-1,-6,7]],4,5,-6,-7,8,9,-10]

uusjärj = rek_abs(järjend)
print(uusjärj)