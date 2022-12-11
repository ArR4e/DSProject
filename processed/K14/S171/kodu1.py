def rek_abs(input):
    li = []
    for x in range(len(input)):
        if isinstance(input[x], list):
            li.append(rek_abs(input[x]))
        else:
            li.append(abs(input[x]))
    return li

print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))