
def rek_abs(järj, uus =[]):
    if not järj:
        return uus
    elif type(järj[0]) == list:
        tükk = []
        uus.append(rek_abs(järj[0], tükk))
    else:
        uus.append(abs(järj[0]))
    return rek_abs(järj[1:], uus)
        
