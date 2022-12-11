
def seosta_lapsed_ja_vanemad(f1, f2):
    with open(f1, encoding="UTF-8") as f1:
        with open(f2, encoding="UTF-8") as f2:
            nimed = {}
            for rida in f2:
                line = rida.strip().split()
                nimed[line[0]] = f"{line[1]} {line[2]}"
            lapsed = {}
            for rida in f1:
                line = rida.strip().split()
                if nimed[line[1]] not in lapsed:
                    hulk = set()
                    hulk.add(nimed[line[0]])
                    lapsed[nimed[line[1]]] = hulk
                else:
                    lapsed[nimed[line[1]]].add(nimed[line[0]])
            return lapsed
        
d = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
for k, v in d.items():
    print(f"{k}: {', '.join(v)}")
