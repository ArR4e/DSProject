a = float(input('Sisesta oma aastatulu'))
tulu = 0
if a <= 6000:
    continue
    print(round(a,2))
if a > 6000 and a <= 14400:
    print(6000)
if a > 14400 and a <= 25200:
    b=6000 - (6000 / 10800) * (a - 14400)
    print(round(b,2))
if a > 25200:
    print(0)
