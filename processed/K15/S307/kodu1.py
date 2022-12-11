import re



fail = open('aadressid.txt', 'r')
andmed = []
print("Kasutajanimed on:")
for line in fail:
    nimi = re.search("http://www.ut.ee/~(.*?)/", line)
    if nimi:
            if " " in (nimi.group(1)):
                pass
            else:
                print(nimi.group(1))