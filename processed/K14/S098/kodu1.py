def rek_abs(rida):
    riit = []
    for i in rida:
        if isinstance(i, list):
            riit.append(rek_abs(i))
        else:
            riit.append(abs(i))
    return riit

print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))