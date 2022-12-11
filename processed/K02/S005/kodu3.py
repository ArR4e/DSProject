firstname = input("Eesnimi?").lower()
lastname = input("Perekonnanimi?").lower()

# handling unaccepted letters

# seda saab teha ka regexiga, aga üldiselt hea tava on üldse kasutada teeki Flashtext
def letterhandler(word):
    return word.replace("õ", "o").replace("ä", "a").replace("ö", "o").replace("ü", "u").replace(" ", "").strip()

firstname = letterhandler(firstname)
lastname = letterhandler(lastname)

print(firstname + "." + lastname)