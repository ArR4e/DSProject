a = [2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]
def rek_abs(jarjend):
    temp = []
    if jarjend == []:
        return temp
    else:
        for i in jarjend:
            if not isinstance(i, list):
                if i < 0:
                    temp.append(-i)
                else:
                    temp.append(i)
            else:
                temp.append(rek_abs(i))
                
    return temp

print(rek_abs(a))