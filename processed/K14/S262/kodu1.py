def rek_abs(jarjend):
    tagasta = []
    for el in jarjend:
        if isinstance(el,list):
            tagasta.append(rek_abs(el))
        else:
            if el >= 0:
                tagasta.append(el)
            else:
                tagasta.append(abs(el))
    return(tagasta)
print(rek_abs([2,-6,[8,-12,-12,[4,[-6],-3]],7,[3.55, -3.55]]))