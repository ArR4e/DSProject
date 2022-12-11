import re

print("Kasutajanimed on:")
with open("aadressid.txt", "r", encoding="UTF-8") as f:
    for line in f:
        line = line.strip()
        if re.search("http://www.ut.ee/~", line):
            tilde_index = line.find('~') + 1
            end_index = line[tilde_index + 1:].find('/')
            kasutajanimi = line[tilde_index:end_index + tilde_index + 1]
            if ' ' not in kasutajanimi:
                print(kasutajanimi)