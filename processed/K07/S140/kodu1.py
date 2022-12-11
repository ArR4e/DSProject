def poisse_ja_tüdrukuid(a):
    p = 0
    t = 0
    for i in a:
        if i[-1].lower() == "p":
            p += 1
        elif i[-1].lower() == "t":
            t += 1
        else:
            print("Sõnest", str(i), "ei ole võimalik välja lugeda, kas tegu on poisi või tüdrukuga.")
    return (p, t)
