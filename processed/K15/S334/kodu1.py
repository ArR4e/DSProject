def get_names():
    with open("aadressid.txt") as f:
        _list = []
        for line in f.readlines():
            line = line.split('http://www.ut.ee/~')
            try:
                _list.append(line[1].split("/")[0])
            except:
                pass
    return _list
names = get_names()
print("Kasutajanimed on: ", *names, sep="\n")
