def rek_abs(jjjärjend):
    tulemus = []
    if isinstance(jjjärjend, list) == False:
        return abs(jjjärjend)
    else:
        for järjend in jjjärjend:
            tulemus.append(rek_abs(järjend))
        return tulemus