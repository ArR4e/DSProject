def seosta_lapsed_ja_vanemad(lapsed, nimed):
    parentChild = list()
    idNames = dict()

    with open(lapsed, encoding="UTF-8") as f:
        for i in f.readlines():
            l = i.strip().split(" ")
            parentChild.append([l[0], l[1]])

    print(parentChild)
    with open(nimed, encoding="UTF-8") as f:
        for i in f.readlines():
            l = i.strip().split(" ")
            idNames[l[0]] = " ".join(l[1:])

    childParents = dict()

    for i in parentChild:
        childParents[i[1]] = set()

    for child in childParents:
        for pair in parentChild:
            if pair[1] == child:
                childParents[child].add(idNames[pair[0]])

    names = dict()

    for childId in childParents:
        names[idNames[childId]] = childParents[childId]

    return names

relations = seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")

for r in relations:
    print(f"{r}: {', '.join(relations[r])}")
