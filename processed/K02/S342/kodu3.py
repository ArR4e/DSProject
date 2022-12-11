import unicodedata
eesnimi = str(input("Sisestage eesnimi: "))
perenimi = str(input("Sisestage perenimi: "))
username = eesnimi.lower() + "." + perenimi.lower()

def removeaccent(text):
    
        text = unicodedata.normalize("NFD", text)\
               .encode("ascii", "ignore")\
               .decode("utf-8")
        return str(text)

output = removeaccent(username)
print(output)