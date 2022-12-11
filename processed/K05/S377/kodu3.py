def voimalik_suurkarp(karp,kogus):
    kogus5=min(kogus//5,karp)
    return kogus5

def voimalik_vaikekarp(karp,kogus):
    kogus1=min(kogus//1,karp)
    return kogus1


def moos(suur,vaike,kogus):
    #suur karp mahutab 5kg
    #väike karp mahutab 1kg
    makskogus=suur*5+vaike*1
    if makskogus>=kogus:
        x=voimalik_suurkarp(suur,kogus)
        y=kogus-x*5
        z=voimalik_vaikekarp(vaike,y)
        if x*5+z*1==kogus:
            return x+z
        else:
            return -1

    else:
        return -1