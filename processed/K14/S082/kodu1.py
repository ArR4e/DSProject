def rek_abs(järjend, uus = []):
    for a in järjend:
        if isinstance(a, list) == True:
            vahepealne = []
            vahepealne = rek_abs(a, vahepealne)
            uus.append(vahepealne)
        else:
            uus.append(abs(a))
    return uus
print(rek_abs([]))