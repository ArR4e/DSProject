
def suurväike(sona):
    from random import randint
    vahetatudsona = sona.swapcase()
    symbolid = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    suvalinenr = randint(0,28)
    suvasymbol = symbolid[suvalinenr]
    for sym in vahetatudsona:
        if sym in symbolid:
            vahetatudsona = vahetatudsona.replace(sym, suvasymbol)
    return(vahetatudsona)