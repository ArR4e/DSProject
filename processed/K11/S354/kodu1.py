def f(lapsefail,nimefail):
    f_lapsed = open(lapsefail, 'r')
    f_nimed = open(nimefail, 'r')
    vl = []



    son = {}

    for rea in f_nimed:
        re = rea.strip()
        re = re.split()
        nimi = re[1] + ' ' + re[2]
        key = re[0]
        son[key] = nimi

    s = {}
    for rida in f_lapsed:
        r = rida.strip().split()
        if r[1] in s.keys():
            s[r[1]] = (s[r[1]], r[0])
        else:
            s[r[1]] = r[0]
    sõnastik = {}
    for laps,vanem in s.items():
        hulk = set()
        if type(vanem) == tuple:
            vanem1, vanem2 = vanem
            hulk.add(son[vanem1])
            hulk.add(son[vanem2])
        else:
            hulk.add(son[vanem])
        sõnastik[son[laps]] = hulk
    return sõnastik
