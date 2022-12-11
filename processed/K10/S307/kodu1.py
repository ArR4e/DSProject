def erinevad_sümbolid(a):
    h1 = set(a)
    return h1

def sümbolite_sagedus(b):
    h2 = dict()
    for letter in b:
        h2[letter] = b.count(letter)
    return h2


def grupeeri(c):
    h3 = {}
    th = set()
    kh = set()
    m = set()
    täishäälikud = 'aeiouõäöüAEIOUÕÄÖÜ'
    kaashäälikud = 'bdfghjklmnprsšzžtvBDFGHJKLMNPRSŠZŽTVxXqQwWcCyY'
    for letter in c:
        if letter in täishäälikud:
            th.add((letter, c.count(letter)))
        elif letter in kaashäälikud:
            kh.add((letter, c.count(letter)))
        else:
            m.add((letter, c.count(letter)))
    h3['Täishäälikud'] = th
    h3['Kaashäälikud'] = kh
    h3['Muud'] = m
    return h3
    