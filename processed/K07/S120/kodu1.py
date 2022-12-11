def poisse_ja_tüdrukuid(lst):
    men = 0
    women = 0
    for person in lst:
        if person.endswith('P'):
            men += 1
        elif person.endswith('T'):
            women += 1
    return men, women