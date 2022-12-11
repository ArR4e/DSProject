rek_abs = lambda jarjend : list(map(lambda x: abs(x) if not(isinstance(x, list)) else rek_abs(x), jarjend ))
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))