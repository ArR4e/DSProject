import re
print("Kasutajanimed on: ")
fail = open('aadressid.txt', 'r', encoding='utf-8')
for rida in fail:
    kasutajanimi = re.search("ut['.']ee/~(\w+)/", rida)
    if kasutajanimi:
        print(kasutajanimi.group(1))