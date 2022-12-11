#mirjampirn
def rek_abs(jarjend):
    uus_jarjend=[]
    for element in jarjend:
        if isinstance(element,list):
            uus_jarjend.append(rek_abs(element))
        else:
            if element<0:
                element1=element*(-1)
            else:
                element1=element
            uus_jarjend.append(element1)
    return uus_jarjend