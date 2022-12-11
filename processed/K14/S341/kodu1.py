def rek_abs(list1):
    uus_list= []
    for element in list1:
        if isinstance(element,list):
            uus_list.append(rek_abs(element))
        else:
            uus_list.append(abs(element))
    return uus_list

print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))