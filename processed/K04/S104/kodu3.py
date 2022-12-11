def summa():
    u = float(input('Sisesta esimese keha kiirus sinu suhtes km/s: '))
    if u < 0:
        return ('kiirus pole negatiivne')
    else:
        v = float(input('Sisesta teise keha kiirus esimese keha suhtes km/s: '))
        if v < 0:
            return ('kiirus pole negatiivne')
        else:
            summa == (u + v)/(1 + u * v / 299792.458)
            print(summa)
                    
#ma ei tea mul ei tööta see isegi kahega ma ei oska :((((
            