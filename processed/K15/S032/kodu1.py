import re
f = open("aadressid.txt", encoding = "UTF-8")
for rida in f:
    match = re.search("ut\.ee/~\w+/", rida)
    if match:
        kasutaja = match[0]
        print(kasutaja[7:-1])
    
f.close()