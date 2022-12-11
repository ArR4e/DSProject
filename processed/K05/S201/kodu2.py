def suurväike(sone):
    import re
    import random
    import string
    uus = re.sub(r"[a-zA-Z]",lambda x :  x.group(0).upper()
                                    if x.group(0).islower()
                                    else x.group(0).lower(),sone)
    t = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in range(0,1):
        b = random.choice(t)
    for a in uus:
        if a in t:
            uus = uus.replace(a, b)
    return(uus)
