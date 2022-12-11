def rek_abs(x):
    for i in range(len(x)):
        if isinstance(x[i-1], list):
            x[i-1] = rek_abs(x[i-1])
        else:
            x[i-1] = abs(x[i-1])
    return x