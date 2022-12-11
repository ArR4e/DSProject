import re
fail=open("aadressid.txt", "r",encoding="UTF-8")
print("Kasutajanimed on:")
for rida in fail:
    leidumine=re.search(r'://www.ut.ee/~([\w.-]+)', rida)
    if leidumine:
        print(leidumine.group(1))
fail.close()