def rek_abs(järjend):
    absoluutv_list=[]
    for element in järjend:
        if isinstance(element,float) or isinstance(element,int):
            absoluutv_list.append(abs(element))
        else:
            absoluutv_list.append(rek_abs(element))
    return absoluutv_list