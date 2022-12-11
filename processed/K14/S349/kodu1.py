def rek_abs(järjend):
    absojärjend=[]
    for element in järjend:
        if isinstance(element, list):
            absojärjend.append(rek_abs(element))
        else:
            absojärjend.append(abs(element))
    return absojärjend

print(rek_abs([2,-6, [8,-12,-12, [4, [-6], -3]], 7, [3.55, -3.55]]))

[2, 6, [8, 12, 12, [4, [6], 3]], 7, [3.55, 3.55]]