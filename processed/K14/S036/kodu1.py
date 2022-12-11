def rek_abs(lst):
    uus_lst =[]
    if lst==[]:
        return lst
    for i in range(len(lst)):
        if isinstance(lst[i],list):
            uus_lst += [rek_abs(lst[i])]
        else:
            uus_lst += [abs(lst[i])]
    
   
    return uus_lst

print(rek_abs([2, -6, [8, -12, [-12]], 7, []]))