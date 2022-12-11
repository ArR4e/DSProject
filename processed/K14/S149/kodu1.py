def rek_abs(järjend):
    if isinstance(järjend, list):
        järjend = järjend.copy()
        for i in range(len(järjend)):
            järjend[i] = rek_abs(järjend[i])
        return järjend
    else:
        return abs(järjend)