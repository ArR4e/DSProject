järjend=[1,-2,-3, 4,-5, 6]
def rek_abs(järjend):
    uusjärjend=[]
    for element in järjend:
        
        if element>=0:
            uusjärjend.append(element)
        else:
            uuselement=(-1)*element
            uusjärjend.append(uuselement)

    return uusjärjend
print(rek_abs(järjend))