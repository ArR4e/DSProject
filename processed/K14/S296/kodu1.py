
def rek_abs(arv):
    s = []
    if arv == []:
        return []
    else:
        for i in range(len(arv)):
            if isinstance(arv[i],list) == False:
                s.append(abs(arv[i]))
            elif isinstance(arv[i],list) == True:
                s.append(rek_abs(arv[i]))
                
        return s

print(rek_abs([1,[-1,2,-3]]))