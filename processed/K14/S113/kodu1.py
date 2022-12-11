def rek_abs(sisend):
    vastus = []
    for number in sisend:
        if isinstance(number, list):
            vastus.append(rek_abs(number))
        else:
            vastus.append(abs(number))
    return vastus