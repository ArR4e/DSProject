def väljasta_liin(ancestor, descendant, tree):
    if ancestor != descendant:
        for i in tree:
            if descendant == i:
                if väljasta_liin(ancestor, tree[i][0], tree):
                    print(descendant)
                    return True
                elif väljasta_liin(ancestor, tree[i][1], tree):
                    print(descendant)
                    return True
        return False # Ei leidu liin
    else:
        print(descendant)
        return True  # Baas