def rek_abs(järjend):
    if len(järjend) == 0:
        return []
    else:
        päis = järjend[0]
        saba = järjend[1:]
        
        d = rek_abs(saba)
        
        if isinstance(päis, (int, float)):
            return [abs(päis)] + d
        else:
            return [rek_abs(päis)] + d