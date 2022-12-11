def rek_abs(s):
    if isinstance(s,list):
        return [rek_abs(x) for x in s]
    else:
        return abs(s)

print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))