def rek_abs(järjend):
    return [abs(x) if not isinstance(x, list) else rek_abs(x) for x in järjend]