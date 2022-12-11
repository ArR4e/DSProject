def erinevad_sümbolid(lause):
    unique = set()
    for i in lause:
        unique.add(i)

    return unique

def sümbolite_sagedus(lause):
    freq = dict()
    for i in lause:
        try:
            freq[i] += 1
        except:
            freq[i] = 1
    return freq

def grupeeri(lause):
    freq = dict()
    freq["Täishäälikud"] = set()
    freq["Kaashäälikud"] = set()
    freq["Muud"] = set()
    wordfreq = dict()

    vow = ["a", "e", "i", "o", "u", "õ", "ä", "ö", "ü"]
    nonvow = ["b", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "š", "z", "ž", "t", "v", "y", "q", "c", "x", "w"]

    for i in lause:
        try:
            wordfreq[i] += 1
        except:
            wordfreq[i] = 1

    for i in wordfreq:
        if i.lower() in vow:
            freq["Täishäälikud"].add((i, wordfreq[i]))
        elif i.lower() in nonvow:
            freq["Kaashäälikud"].add((i, wordfreq[i]))
        else:
            freq["Muud"].add((i, wordfreq[i]))

    return freq
