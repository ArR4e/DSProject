
def rek_abs(n):

    k = list()
    
    if not isinstance(n, list):
        return abs(n)

    elif isinstance(n, list):
        for i in n:
            if not isinstance(i, list):
                k.append(abs(i))
            else:
                k.append(rek_abs(i))
        return k
