def rek_abs(järjend):
    uus_järjend = []
    for a in range(len(järjend)):
        try:
            if järjend [a] < 0:järjend [a]= järjend [a] - 2 * järjend [a]
        except:
            rek_abs(järjend [a])
    return järjend
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))
