def suurväike(abc):
    for a in abc:
        if a.isupper():
            b = a.lower()
        elif a.islower():
            b = a.upper()
        elif a == " ":
            b = " "
        else:
            b = "&"
        print(b, end="")
tekst = str(input("Sisesta midagi, milles on suured tähed, väiksed tähed, kirjavahemärgid ja tühikud: "))
suurväike(tekst)