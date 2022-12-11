import re

print("Kasutajanimed on:")

fail = open('aadressid.txt')
for rida in fail:
    # leiab sobivad veebiaadressid (TÜ algusega + kasutajanimi)
    leitud = re.findall(r"http:\/\/www\.ut\.ee\/~[a-z,A-Z,0-9]*\/", rida)
    if len(leitud) == 0:
        continue
    aadress = leitud[0]
    leitud2 = re.findall(r"~[a-z,A-Z,0-9]+\/", aadress)
    kasutajanimi = leitud2[0]
    kasutajanimi = kasutajanimi[1:-1]
    print(kasutajanimi)
    